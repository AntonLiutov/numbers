# Numbers

A frontend-only random number generator web app for work item `F1`. The app renders a single stylish browser experience, generates one whole number from `1` to `100` on user interaction, and builds to a static `dist/` bundle.

## Requirements Coverage

- One clear primary interaction for generation
- Exactly one current whole number from `1` to `100`
- Repeat generation without reload
- Stylish modern visual treatment
- Fast, simple, static deployment shape with no backend

## Project Structure

- `src/` source HTML, CSS, and JavaScript
- `dist/` generated static build output
- `tools/` local Python build and static-serve helpers

## Run Locally

With `uv`:

```bash
uv run python tools/build_static.py
uv run python tools/serve_static.py
```

Then open `http://127.0.0.1:8000`.

Without `uv`:

```bash
python tools/build_static.py
python tools/serve_static.py
```

## Docker

```bash
docker compose up --build
```

Then open `http://127.0.0.1:8000`.

## Notes

- No secrets are required for this app.
- The deployed artifact is the static `dist/` folder.
