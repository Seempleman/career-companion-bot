#!/usr/bin/env python3
"""Produce a source-linked project checkpoint without an AI service."""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def main() -> None:
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    source_commit = git("rev-parse", "HEAD")
    repository = "https://github.com/Seempleman/career-companion-bot"
    manifest = json.loads(Path("RELEASE_MANIFEST.json").read_text(encoding="utf-8"))
    context = Path("PROJECT_CONTEXT.md").read_text(encoding="utf-8")
    recent = [
        {"sha": row.split("\x1f", 1)[0], "subject": row.split("\x1f", 1)[1]}
        for row in git("log", "-10", "--format=%h%x1f%s").splitlines()
        if "\x1f" in row
    ]
    tracked_files = git("ls-files").splitlines()
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")

    record = {
        "product": "Career Companion Bot",
        "checkpoint_schema_version": 1,
        "created_at_utc": timestamp,
        "official_repository": repository,
        "source_branch": "main",
        "source_commit": source_commit,
        "framework_version": manifest.get("version"),
        "release_status": manifest.get("release_status"),
        "manifest_schema_version": manifest.get("schema_version"),
        "manifest_tracked_files": len(manifest.get("files", {})),
        "repository_file_count": len(tracked_files),
        "repository_files": tracked_files,
        "recent_commits": recent,
        "project_context_file": "PROJECT_CONTEXT.md",
        "entrypoint_file": "START_HERE.md",
        "maintainer_prompt_file": "MAINTAINER_PROMPT.txt",
        "source_tree_url": repository + "/tree/" + source_commit,
    }

    lines = [
        "# Career Companion Bot Project Checkpoint",
        "",
        "This checkpoint was generated automatically from the main branch. It is a navigation and state digest, not a replacement for source instructions.",
        "",
        "Source commit: " + source_commit,
        "Generated (UTC): " + timestamp,
        "Framework version: " + str(manifest.get("version")),
        "Release status: " + str(manifest.get("release_status")),
        "Source repository: " + repository,
        "Source tree: " + record["source_tree_url"],
        "",
        "## Maintained product context",
        "",
        context.strip(),
        "",
        "## Recent commits",
        "",
    ]
    lines.extend("* " + item["sha"] + ": " + item["subject"] for item in recent)
    lines.extend([
        "",
        "## Source file inventory",
        "",
    ])
    lines.extend("* " + name for name in tracked_files)
    lines.extend([
        "",
        "## Freshness and trust",
        "",
        "Before continuing development, compare the source commit above with the latest main commit. If they differ, treat this checkpoint as stale and inspect main directly.",
        "Read the latest relevant framework files and changelog before modifying anything. Do not assume that this digest contains every rule or outstanding issue.",
        "This auto generated record is not a signed release and is not cryptographic proof of publisher identity.",
        "",
    ])
    (out / "PROJECT_CHECKPOINT.md").write_text("\n".join(lines), encoding="utf-8")
    (out / "PROJECT_CHECKPOINT.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
