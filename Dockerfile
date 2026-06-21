FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv uv sync --frozen --no-dev

COPY src ./src
COPY tools ./tools
COPY .env.example ./

RUN uv run --no-sync python tools/build_static.py

EXPOSE 8000

CMD ["uv", "run", "--no-sync", "python", "tools/serve_static.py", "--host", "0.0.0.0", "--port", "8000", "--directory", "dist"]
