from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Serve the built static site.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8000, type=int)
    parser.add_argument("--directory", default="dist")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    directory = (PROJECT_ROOT / args.directory).resolve()
    handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"Serving {directory} on http://{args.host}:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
