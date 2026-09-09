#!/usr/bin/env python3
"""Checkpoint-aware, provenance-safe impact analysis for Ubuntu Capital monitoring.

V4 fixes four remaining blind spots in V3:
1. PR commit membership is compared to the previous monitor checkpoint instead of
   using commit author/committer dates.
2. PR commit inspection uses local git objects, avoiding GitHub's 250-commit PR
   endpoint cap and omitted `patch` fields on oversized diffs.
3. Existing PR title/body edits are detected by comparing current metadata to the
   previous successful run's state.
4. The current open-PR snapshot is persisted as `monitoring-output/state.json` and
   is carried by the existing 7-day workflow artifact for the next run.
"""

from __future__ import annotations

import io
import json
import re
import urllib.request
import zipfile
from pathlib import Path

import repository_monitor as base
import repository_monitor_v2 as v2
import repository_monitor_v3 as v3

ORIGINAL_COLLECT_PR_ACTIVITY = base.collect_pr_activity
STATE_PATH = Path(base.OUT_DIR) / "state.json"
_STATE_CACHE: dict | None = None


def _download_bytes(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {base.TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ubuntu-capital-os-monitor",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def previous_successful_run_id(branch: str) -> int | None:
    current = base.api(f"/repos/{base.REPO}/actions/runs/{base.RUN_ID}")
    workflow_id = current["workflow_id"]
    page = 1
    while True:
        data = base.api(
            f"/repos/{base.REPO}/actions/workflows/{workflow_id}/runs",
            {"branch": branch, "status": "completed", "per_page": 100, "page": page},
        )
        runs = data.get("workflow_runs", []) if isinstance(data, dict) else []
        if not runs:
            return None
        for run in runs:
            if str(run.get("id")) == str(base.RUN_ID):
                continue
            if run.get("conclusion") == "success" and run.get("id"):
                return int(run["id"])
        if len(runs) < 100:
            return None
        page += 1


def load_previous_monitor_state() -> dict:
    global _STATE_CACHE
    if _STATE_CACHE is not None:
        return _STATE_CACHE

    _STATE_CACHE = {}
    try:
        branch = base.repository_default_branch()
        run_id = previous_successful_run_id(branch)
        if not run_id:
            return _STATE_CACHE
        data = base.api(f"/repos/{base.REPO}/actions/runs/{run_id}/artifacts", {"per_page": 100})
        artifacts = data.get("artifacts", []) if isinstance(data, dict) else []
        artifact = next(
            (
                item
                for item in artifacts
                if not item.get("expired")
                and str(item.get("name", "")).startswith("ubuntu-capital-repository-monitor-")
                and item.get("archive_download_url")
            ),
            None,
        )
        if not artifact:
            return _STATE_CACHE
        payload = _download_bytes(artifact["archive_download_url"])
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            state_name = next((name for name in archive.namelist() if name.endswith("state.json")), None)
            if state_name:
                _STATE_CACHE = json.loads(archive.read(state_name).decode("utf-8"))
    except Exception:
        _STATE_CACHE = {}
    return _STATE_CACHE


def snapshot_open_pull_requests() -> dict:
    snapshots: dict[str, dict] = {}
    page = 1
    while True:
        batch = base.api(
            f"/repos/{base.REPO}/pulls",
            {"state": "open", "sort": "updated", "direction": "desc", "per_page": 100, "page": page},
        )
        if not isinstance(batch, list) or not batch:
            break
        for pr in batch:
            number = pr.get("number")
            if not number:
                continue
            snapshots[str(number)] = {
                "head_sha": (pr.get("head") or {}).get("sha"),
                "title": pr.get("title") or "",
                "body": pr.get("body") or "",
                "updated_at": pr.get("updated_at"),
            }
        if len(batch) < 100:
            break
        page += 1
    return snapshots


def write_monitor_state() -> None:
    state = {
        "version": 1,
        "repository": base.REPO,
        "branch": base.repository_default_branch(),
        "pull_requests": snapshot_open_pull_requests(),
    }
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def transition_commits(previous_head: str, current_head: str) -> tuple[list[str], dict | None]:
    if not previous_head or not current_head or previous_head == current_head:
        return [], None
    if not base.ensure_commit_available(previous_head) or not base.ensure_commit_available(current_head):
        return [], {"previous_head": previous_head, "current_head": current_head, "kind": "unavailable"}
    if base.git_is_ancestor(previous_head, current_head):
        raw = base.git("rev-list", "--reverse", f"{previous_head}..{current_head}")
        return [sha for sha in raw.splitlines() if sha.strip()], None
    return [], {"previous_head": previous_head, "current_head": current_head, "kind": "rewritten"}


def pr_window_provenance(number: int, since) -> dict:
    detail = base.api(f"/repos/{base.REPO}/pulls/{number}")
    created_at = detail.get("created_at")
    merged_at = detail.get("merged_at")
    created = bool(created_at and base.parse_dt(created_at) >= since)
    merged = bool(merged_at and base.parse_dt(merged_at) >= since)

    previous = load_previous_monitor_state().get("pull_requests", {}).get(str(number))
    current_head = (detail.get("head") or {}).get("sha")
    metadata_changes: list[dict] = []
    commit_shas: list[str] = []
    head_rewrite = None

    if previous:
        if (previous.get("title") or "") != (detail.get("title") or ""):
            metadata_changes.append(
                {
                    "field": "title",
                    "before": previous.get("title") or "",
                    "after": detail.get("title") or "",
                }
            )
        if (previous.get("body") or "") != (detail.get("body") or ""):
            metadata_changes.append(
                {
                    "field": "body",
                    "before": previous.get("body") or "",
                    "after": detail.get("body") or "",
                }
            )
        previous_head = previous.get("head_sha")
        if previous_head and current_head and previous_head != current_head:
            commit_shas, head_rewrite = transition_commits(previous_head, current_head)

    if created:
        mode = "created"
    elif merged:
        mode = "merged"
    elif previous and (metadata_changes or commit_shas or head_rewrite):
        mode = "checkpoint_delta"
    elif previous:
        mode = "none"
    else:
        mode = "unverified"

    return {
        "mode": mode,
        "detail": detail,
        "commit_shas": commit_shas,
        "metadata_changes": metadata_changes,
        "head_rewrite": head_rewrite,
    }


def collect_pr_activity_with_checkpoint(since):
    items = ORIGINAL_COLLECT_PR_ACTIVITY(since)
    for item in items:
        number = item.get("number")
        if not number:
            item["material_pr_activity"] = "none"
            continue
        try:
            provenance = pr_window_provenance(number, since)
            item["material_pr_activity"] = provenance["mode"]
            item["material_pr_detail"] = provenance["detail"]
            item["material_pr_commit_shas"] = provenance["commit_shas"]
            item["material_pr_metadata_changes"] = provenance["metadata_changes"]
            item["material_pr_head_rewrite"] = provenance["head_rewrite"]
        except Exception as exc:
            item["material_pr_activity"] = "unverified"
            item["material_pr_verification_error"] = type(exc).__name__
    return items


def local_commit_evidence(sha: str) -> tuple[dict, str, list[dict]]:
    if not base.ensure_commit_available(sha):
        raise RuntimeError(f"Commit {sha} is unavailable for local evidence inspection.")
    message = base.git("show", "-s", "--format=%B", sha).strip()
    files, _ = base.commit_files_and_patch(sha)
    item = {
        "sha": sha,
        "short": sha[:7],
        "message": message.splitlines()[0] if message else "PR commit",
        "files": files,
    }
    return item, message, v2.commit_file_evidence(item)


def compare_file_evidence(previous_head: str, current_head: str) -> list[dict]:
    if not base.ensure_commit_available(previous_head) or not base.ensure_commit_available(current_head):
        return []
    status_raw = base.git("diff", "--name-status", "-M", "--no-ext-diff", previous_head, current_head)
    files = base.parse_name_status(status_raw)
    evidence: list[dict] = []
    for file_entry in files:
        filename = file_entry.get("filename")
        previous_filename = file_entry.get("previous_filename")
        paths = [path for path in (previous_filename, filename) if path]
        if not paths:
            continue
        patch = base.git(
            "diff",
            "--format=",
            "--unified=0",
            "--no-ext-diff",
            previous_head,
            current_head,
            "--",
            *paths,
        )
        ids = v2.ids_in_changed_lines(patch)
        for path in paths:
            ids.update(re.findall(base.USE_CASE_PATTERN, path))
        evidence.append({"paths": paths, "ids": ids})
    return evidence


def full_pr_file_evidence(detail: dict) -> list[dict]:
    base_sha = (detail.get("base") or {}).get("sha")
    head_sha = (detail.get("head") or {}).get("sha")
    if not base_sha or not head_sha:
        return []
    if not base.ensure_commit_available(base_sha) or not base.ensure_commit_available(head_sha):
        return []
    comparison_base = base.git_merge_base(base_sha, head_sha) or base_sha
    return compare_file_evidence(comparison_base, head_sha)


def material_use_case_changes(catalogue: dict[str, str], commits, pull_requests, rewrite=None):
    v2.IMPACT_RECORDS.clear()
    v2.BROAD_REFERENCES.clear()
    v2.ABSENT_DIRECT_IDS.clear()
    all_direct_ids: set[str] = set()

    for item in commits:
        message = v3.full_commit_message(item)
        observed_metadata_ids = set(re.findall(base.USE_CASE_PATTERN, message))
        metadata_ids = v3.record_metadata_signals(item, message, "commit metadata")
        all_direct_ids.update(metadata_ids)

        file_evidence = v2.commit_file_evidence(item)
        observed_file_ids = {uid for evidence in file_evidence for uid in set(evidence.get("ids", set()))}
        direct_file_ids = v3.record_file_signals_per_file(item, file_evidence)
        all_direct_ids.update(direct_file_ids)

        residual = set(item.get("use_case_ids", [])) - observed_metadata_ids - observed_file_ids
        if residual:
            v2.BROAD_REFERENCES.append(
                {
                    "source": v2.source_label(item) + " — unattributed commit references",
                    "files": [],
                    "ids": sorted(residual),
                }
            )

    for item in pull_requests:
        mode = item.get("material_pr_activity", "unverified")

        if mode in {"none", "unverified"}:
            residual = set(item.get("use_case_ids", []))
            if residual:
                reason = "comment/review-only or unchanged PR evidence"
                if mode == "unverified":
                    reason = "checkpoint provenance unavailable"
                v2.BROAD_REFERENCES.append(
                    {
                        "source": v2.source_label(item) + f" — {reason}",
                        "files": [],
                        "ids": sorted(residual),
                    }
                )
            continue

        detail = item.get("material_pr_detail") or {}
        if mode in {"created", "merged"}:
            title_ids = v3.record_metadata_signals(
                item,
                detail.get("title") or item.get("title") or "",
                "PR title metadata",
                always_direct=True,
            )
            body_ids = v3.record_metadata_signals(item, detail.get("body") or "", "PR body metadata")
            all_direct_ids.update(title_ids | body_ids)
            all_direct_ids.update(v3.record_file_signals_per_file(item, full_pr_file_evidence(detail)))
            continue

        if mode == "checkpoint_delta":
            for change in item.get("material_pr_metadata_changes", []):
                field = change.get("field", "metadata")
                text = (change.get("before") or "") + "\n" + (change.get("after") or "")
                ids = v3.record_metadata_signals(
                    item,
                    text,
                    f"PR {field} metadata changed in-window",
                    always_direct=(field == "title"),
                )
                all_direct_ids.update(ids)

            for sha in item.get("material_pr_commit_shas", []):
                try:
                    commit_item, message, file_evidence = local_commit_evidence(sha)
                except Exception:
                    continue
                all_direct_ids.update(
                    v3.record_metadata_signals(commit_item, message, "new PR commit metadata")
                )
                all_direct_ids.update(v3.record_file_signals_per_file(commit_item, file_evidence))

            head_rewrite = item.get("material_pr_head_rewrite")
            if head_rewrite and head_rewrite.get("kind") == "rewritten":
                synthetic = {
                    "number": item.get("number"),
                    "title": (item.get("title") or "") + " — PR head rewrite",
                    "files": [],
                }
                evidence = compare_file_evidence(
                    head_rewrite.get("previous_head", ""),
                    head_rewrite.get("current_head", ""),
                )
                all_direct_ids.update(v3.record_file_signals_per_file(synthetic, evidence))
            continue

    if rewrite:
        synthetic = {
            "number": "history",
            "title": f"default-branch {rewrite.get('kind', 'rewrite')}",
            "files": rewrite.get("files", []),
        }
        direct_rewrite_ids = v3.record_file_signals_per_file(
            synthetic, v3.rewrite_file_evidence(rewrite)
        )
        all_direct_ids.update(direct_rewrite_ids)
        residual_rewrite = set(rewrite.get("use_case_ids", [])) - direct_rewrite_ids
        if residual_rewrite:
            v2.BROAD_REFERENCES.append(
                {
                    "source": f"default-branch {rewrite.get('kind', 'rewrite')} — unattributed state references",
                    "files": [],
                    "ids": sorted(residual_rewrite),
                }
            )

    known = sorted(uid for uid in all_direct_ids if uid in catalogue)
    absent = sorted(uid for uid in all_direct_ids if uid not in catalogue)
    v2.ABSENT_DIRECT_IDS.extend(absent)
    return known, absent


def main() -> None:
    base.collect_pr_activity = collect_pr_activity_with_checkpoint
    v2.material_use_case_changes = material_use_case_changes
    v2.main()
    write_monitor_state()


if __name__ == "__main__":
    main()
