from __future__ import annotations

from pathlib import Path
import shutil


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = PROJECT_ROOT / "src"
DIST_DIR = PROJECT_ROOT / "dist"


def build_static_site() -> None:
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    shutil.copytree(SOURCE_DIR, DIST_DIR)


def main() -> None:
    build_static_site()
    print(f"Built static site into {DIST_DIR}")


if __name__ == "__main__":
    main()
