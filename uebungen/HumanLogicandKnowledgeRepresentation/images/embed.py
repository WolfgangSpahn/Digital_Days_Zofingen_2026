#!/usr/bin/env python3
"""
Embed an SVG into an HTML file at a placeholder.

Usage:
    python embed_svg.py index.html graph.svg [output.html]

If [output.html] is omitted, it overwrites index.html.
"""

import sys
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Usage: python embed.py graph.html graph.svg [output.html]")
        sys.exit(1)

    html_path = Path(sys.argv[1])
    svg_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3]) if len(sys.argv) > 3 else "index.html"

    if not html_path.exists():
        print(f"Error: HTML file not found: {html_path}")
        sys.exit(1)
    if not svg_path.exists():
        print(f"Error: SVG file not found: {svg_path}")
        sys.exit(1)

    html_text = html_path.read_text(encoding="utf-8")
    svg_text = svg_path.read_text(encoding="utf-8")

    placeholder = "<!-- INSERT_SVG_HERE -->"
    if placeholder not in html_text:
        print(f"Error: Placeholder '{placeholder}' not found in {html_path.name}")
        sys.exit(1)

    merged_html = html_text.replace(placeholder, svg_text)

    output_path.write_text(merged_html, encoding="utf-8")
    print(f"✅ SVG from '{svg_path.name}' embedded into '{output_path.name}'")

if __name__ == "__main__":
    main()
