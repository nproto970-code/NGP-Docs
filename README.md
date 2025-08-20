
# GitBook Public Downloads Template

A ready-to-sync Git repository for a GitBook space with a public **Downloads** section.
Just add files into `docs/downloads/` and they’ll appear on the Downloads page with
file size, modified date, and direct links.

## Features
- GitBook-compatible Markdown structure (`SUMMARY.md`, `.gitbook.yaml`).
- Auto-generated **Downloads** page via `scripts/generate_downloads.py`.
- Keeps large files out of git by default (`.gitignore`).
- Clean content structure under `docs/`.

## Quick Start
1. **Use this repository as a template** on GitHub (or clone locally).
2. Add or remove files under `docs/downloads/` (PDFs, ZIPs, CSVs, etc.).
3. Run `python3 scripts/generate_downloads.py` to regenerate the Downloads page.
4. Commit & push.
5. In GitBook, create a new Space → **Connect with Git** → select this repo and branch.
6. In GitBook Space settings → **Visibility**, set to **Public** so anyone can download.
7. Publish.

## Adding Files
- Put downloadable assets in: `docs/downloads/`.
- Put images used in pages in: `docs/assets/` and reference them with `![](./assets/...)`.

## Notes
- The index page lives at `docs/index.md` (aliased to `/`).
- GitBook will render the folder structure based on `SUMMARY.md` and `.gitbook.yaml`.
- If you change folder names, update the paths in both files accordingly.

## License
MIT
