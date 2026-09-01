#!/usr/bin/env python3
"""Create a presentation directory from the bundled neutral starter."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--title", default="Presentation title")
    parser.add_argument(
        "--posture",
        choices=("editorial", "cinematic", "hybrid", "operating"),
        default="editorial",
    )
    parser.add_argument("--echarts", type=Path, help="Path to a local echarts.min.js")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    template = skill_root / "assets" / "starter" / "deck.html"
    output_dir = args.output_dir.resolve()
    output_file = output_dir / "index.html"

    if output_file.exists() and not args.force:
        parser.error(f"{output_file} exists; pass --force to replace it")

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "assets").mkdir(exist_ok=True)
    html = template.read_text(encoding="utf-8")
    html = html.replace("{{DECK_TITLE}}", args.title)
    html = html.replace("{{DEFAULT_POSTURE}}", args.posture)
    output_file.write_text(html, encoding="utf-8")

    if args.echarts:
        source = args.echarts.resolve()
        if not source.is_file():
            parser.error(f"ECharts bundle not found: {source}")
        shutil.copy2(source, output_dir / "assets" / "echarts.min.js")

    print(output_file)
    if not (output_dir / "assets" / "echarts.min.js").exists():
        print("Note: add assets/echarts.min.js before using ECharts visuals.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
