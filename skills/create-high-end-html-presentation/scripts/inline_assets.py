#!/usr/bin/env python3
"""Inline local JavaScript and CSS dependencies into a single HTML file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlparse


SCRIPT_RE = re.compile(
    r'<script(?P<before>[^>]*?)\ssrc=["\'](?P<src>[^"\']+)["\'](?P<after>[^>]*)>\s*</script>',
    re.IGNORECASE,
)
STYLE_RE = re.compile(
    r'<link(?=[^>]*\brel=["\']stylesheet["\'])(?=[^>]*\bhref=["\'](?P<href>[^"\']+)["\'])[^>]*>',
    re.IGNORECASE,
)


def local_path(base: Path, reference: str) -> Path | None:
    parsed = urlparse(reference)
    if parsed.scheme or parsed.netloc or reference.startswith("//"):
        return None
    return (base / parsed.path).resolve()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_html", type=Path)
    parser.add_argument("output_html", type=Path)
    args = parser.parse_args()

    input_file = args.input_html.resolve()
    output_file = args.output_html.resolve()
    base = input_file.parent
    html = input_file.read_text(encoding="utf-8")

    def replace_script(match: re.Match[str]) -> str:
        path = local_path(base, match.group("src"))
        if path is None:
            return match.group(0)
        if not path.is_file():
            raise FileNotFoundError(f"Missing script: {path}")
        attrs = f"{match.group('before')}{match.group('after')}".strip()
        attrs = f" {attrs}" if attrs else ""
        return f"<script{attrs}>\n{path.read_text(encoding='utf-8')}\n</script>"

    def replace_style(match: re.Match[str]) -> str:
        path = local_path(base, match.group("href"))
        if path is None:
            return match.group(0)
        if not path.is_file():
            raise FileNotFoundError(f"Missing stylesheet: {path}")
        return f"<style>\n{path.read_text(encoding='utf-8')}\n</style>"

    html = SCRIPT_RE.sub(replace_script, html)
    html = STYLE_RE.sub(replace_style, html)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(html, encoding="utf-8")
    print(output_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
