
#!/usr/bin/env python3
# Generate a Markdown table of files in docs/downloads/ with size and modified date.
# Writes to docs/downloads.md

import os
import pathlib
import datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOWNLOADS_DIR = ROOT / "docs" / "downloads"
OUTPUT_MD = ROOT / "docs" / "downloads.md"

def human_size(n: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(n)
    for u in units:
        if size < 1024.0 or u == units[-1]:
            return f"{size:.1f} {u}"
        size /= 1024.0

def main():
    files = []
    for p in sorted(DOWNLOADS_DIR.glob("**/*")):
        if p.is_file():
            rel = p.relative_to(ROOT / "docs")
            stat = p.stat()
            files.append({
                "name": p.name,
                "path": str(rel).replace("\\", "/"),
                "size": stat.st_size,
                "mtime": datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
            })

    lines = ["# Downloads", ""]
    if not files:
        lines += [
            "No files found yet.",
            "",
            "Add files into `docs/downloads/` then run:",
            "",
            "```bash",
            "python3 scripts/generate_downloads.py",
            "```",
        ]
    else:
        lines += ["| File | Size | Last Modified |", "|---|---:|:---|"]
        for f in files:
            # GitBook serves files under the same relative path; link using the docs path.
            link = f"[{f['name']}]({f['path']})"
            lines.append(f"| {link} | {human_size(f['size'])} | {f['mtime']} |")

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT_MD} with {len(files)} file(s).")

if __name__ == "__main__":
    main()
