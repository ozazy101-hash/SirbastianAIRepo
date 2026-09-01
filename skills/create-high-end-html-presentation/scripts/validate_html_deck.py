#!/usr/bin/env python3
"""Run structural, accessibility, and packaging checks on an HTML presentation."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class Inspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.elements: list[tuple[str, dict[str, str]]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.elements.append((tag, {key: value or "" for key, value in attrs}))


def class_names(attrs: dict[str, str]) -> set[str]:
    return set(attrs.get("class", "").split())


def local_path(value: str, base: Path) -> Path | None:
    parsed = urlparse(value)
    if value.startswith("#") or parsed.scheme in {"data", "mailto", "tel"} or parsed.netloc:
        return None
    if parsed.scheme:
        return None
    return (base / unquote(parsed.path)).resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_file", type=Path)
    parser.add_argument("--strict-self-contained", action="store_true")
    args = parser.parse_args()

    path = args.html_file.resolve()
    html = path.read_text(encoding="utf-8")
    lower = html.lower()
    inspector = Inspector()
    inspector.feed(html)
    errors: list[str] = []
    warnings: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(lower.lstrip().startswith("<!doctype html>"), "missing HTML doctype")
    require(bool(re.search(r"<html\b[^>]*\blang=[\"'][^\"']+[\"']", lower)), "missing html language")
    require(bool(re.search(r"<meta\b[^>]*name=[\"']viewport[\"']", lower)), "missing viewport metadata")
    require("<title>" in lower, "missing document title")
    require("<main" in lower, "missing main landmark")
    require(bool(re.search(r"rel=[\"']icon[\"'][^>]*href=[\"']data:", lower)), "missing self-contained favicon")
    require("keydown" in lower, "missing keyboard navigation")
    require("prefers-reduced-motion" in lower, "missing reduced-motion handling")
    require(":focus-visible" in lower, "missing visible keyboard focus styling")
    require("aria-label" in lower, "missing accessible control labels")
    require(not re.search(r"\{\{[A-Z][A-Z0-9_]*\}\}", html), "unresolved template token")

    slides = [(tag, attrs) for tag, attrs in inspector.elements if "slide" in class_names(attrs)]
    require(len(slides) >= 2, "fewer than two slides")
    active = [attrs for _, attrs in slides if "active" in class_names(attrs)]
    require(len(active) == 1, f"expected exactly one active slide in source; found {len(active)}")

    all_ids = [attrs["id"] for _, attrs in inspector.elements if attrs.get("id")]
    duplicates = sorted({item for item in all_ids if all_ids.count(item) > 1})
    require(not duplicates, f"duplicate element ids: {', '.join(duplicates)}")
    id_set = set(all_ids)
    for index, (_, attrs) in enumerate(slides, start=1):
        slide_id = attrs.get("id")
        require(bool(slide_id), f"slide {index} has no id")
        labelled_by = attrs.get("aria-labelledby")
        require(bool(labelled_by), f"slide {index} has no aria-labelledby")
        if labelled_by:
            require(labelled_by in id_set, f"slide {index} references missing label id: {labelled_by}")

    for tag, attrs in inspector.elements:
        if tag == "button" and not attrs.get("type"):
            warnings.append(f"button without explicit type: {attrs.get('id', 'unnamed')}")

    figures = sum(1 for tag, _ in inspector.elements if tag == "figure")
    captions = sum(1 for tag, _ in inspector.elements if tag == "figcaption")
    if figures > captions:
        errors.append("one or more figures lack figcaption")

    remote: list[str] = []
    linked_local: list[str] = []
    for tag, attrs in inspector.elements:
        attribute = "href" if tag in {"a", "link"} else "src" if tag in {"script", "img", "iframe"} else ""
        if not attribute or not attrs.get(attribute):
            continue
        value = attrs[attribute]
        if value.startswith(("http://", "https://", "//")):
            remote.append(value)
            continue
        local = local_path(value, path.parent)
        if local is not None and tag != "a":
            linked_local.append(value)
            if not local.is_file():
                errors.append(f"missing local dependency: {value}")

    if remote:
        warnings.append(f"remote dependencies: {len(remote)}")
    if args.strict_self_contained and (remote or linked_local):
        errors.append("strict self-contained mode found linked dependencies")
    if "illustrative" not in lower:
        warnings.append("no illustrative-data label found; confirm all figures are sourced")
    if "prototype" not in lower:
        warnings.append("prototype status is not visibly marked")
    if "echarts.init" in lower and "chart-fallback" not in lower:
        warnings.append("ECharts is initialized without a visible fallback")
    if "<figure" in lower and "role=\"img\"" not in lower and "role='img'" not in lower:
        warnings.append("figure content has no stable role=img wrapper")

    for warning in dict.fromkeys(warnings):
        print(f"WARNING: {warning}")
    for error in dict.fromkeys(errors):
        print(f"ERROR: {error}")
    if errors:
        return 1
    print(f"OK: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
