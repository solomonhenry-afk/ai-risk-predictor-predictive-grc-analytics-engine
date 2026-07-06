#!/usr/bin/env python3
"""Create a Task 5 evidence manifest for CI/CD governance runs."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
REPORTS_DIR = BASE_DIR / "reports"
MODELS_DIR = BASE_DIR / "models"

MANIFEST_FILE = OUTPUT_DIR / "task5_evidence_manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    tracked_files = []

    for directory in [OUTPUT_DIR, REPORTS_DIR, MODELS_DIR]:
        if directory.exists():
            for path in sorted(directory.rglob("*")):
                if path.is_file() and path != MANIFEST_FILE:
                    tracked_files.append(
                        {
                            "path": str(path.relative_to(BASE_DIR)),
                            "size_bytes": path.stat().st_size,
                            "sha256": sha256(path),
                        }
                    )

    manifest = {
        "project": "AI Risk Predictor — Predictive GRC Analytics Engine",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "purpose": (
            "Evidence manifest for validated telemetry, model outputs, "
            "threat correlations, explainability, and executive governance reports."
        ),
        "artifact_count": len(tracked_files),
        "artifacts": tracked_files,
    }

    MANIFEST_FILE.write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"[+] Evidence manifest created: {MANIFEST_FILE}")
    print(f"[+] Tracked artifacts: {len(tracked_files)}")


if __name__ == "__main__":
    main()
