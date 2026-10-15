"""Write Packages/<package>/layout.json for the built bridges package.

fspackagetool normally writes it, but build.bat closes the tool as soon as _RPTErrors.xml is rewritten and, for this package, the tool
had not written layout.json by then.  Same format as airport-cyxd/Packages/*/layout.json: every file except layout.json and manifest.json, lower-case
forward-slash path, size in bytes, date as a Windows FILETIME.

    python -I scenery-edmonton-bridges/tools/make_layout.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    for pkg in (ROOT / "scenery-edmonton-bridges" / "Packages").iterdir():
        if not pkg.is_dir():
            continue
        content = []
        for f in sorted(pkg.rglob("*"), key=lambda p: p.relative_to(pkg).as_posix().lower()):
            if f.is_file() and f.name.lower() not in ("layout.json", "manifest.json"):
                st = f.stat()
                content.append({"path": f.relative_to(pkg).as_posix().lower(), "size": st.st_size,
                                "date": int((st.st_mtime + 11644473600) * 10_000_000)})
        (pkg / "layout.json").write_text(json.dumps({"content": content}, indent=2), encoding="utf-8")
        print(pkg.name, len(content), "files")


if __name__ == "__main__":
    main()
