# Numbers

A frontend-only random number generator web app for work items `F1` and `DEPLOY`. The app renders a single stylish browser experience, generates one whole number from `1` to `100` on user interaction, builds to a static `dist/` bundle, and is deployed to an Azure review URL.

## Requirements Coverage

- One clear primary interaction for generation
- Exactly one current whole number from `1` to `100`
- Repeat generation without reload
- Stylish modern visual treatment
- Fast, simple, static deployment shape with no backend

## Review Deployment

Review URL:

- `https://app-agentic-numbers-dev.whitesea-3e028355.eastus.azurecontainerapps.io`

Azure resources used for review hosting:

- Resource group: `rg-agentic-dev`
- Container Apps environment: `agentic-dev-env`
- Container registry: `agenticdevacr`
- Review app: `app-agentic-numbers-dev`

## Project Structure

- `src/` source HTML, CSS, and JavaScript
- `dist/` generated static build output
- `tools/` local Python build and static-serve helpers
- `execution-summary.md` implementation summary for the current delivered work item

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

If you want the server to read the built output explicitly:

```bash
uv run python tools/serve_static.py --directory dist
```

## Docker

```bash
docker compose up --build
```

Then open `http://127.0.0.1:8000`.

## Notes

- No secrets are required for this app.
- `.env.example` is included only to satisfy the project contract; the app does not consume runtime variables.
- The deployed artifact is the static `dist/` folder.
- The current review surface runs on Azure Container Apps using the shared dev environment reuse path captured in the deployment artifacts.
