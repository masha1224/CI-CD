# Polish Sentiment Analysis API

[![CI/CD](https://github.com/masha1224/CI-CD/actions/workflows/ci_cd_workflow.yaml/badge.svg)](https://github.com/masha1224/CI-CD/actions/workflows/ci_cd_workflow.yaml)

REST API for Polish text sentiment classification (positive / neutral / negative), built with FastAPI and a transformer model exported to ONNX for lightweight inference.

## How it works

1. A pre-trained Polish sentiment model ([bardsai/twitter-sentiment-pl-base](https://huggingface.co/bardsai/twitter-sentiment-pl-base)) is downloaded from Hugging Face
2. The model is exported to ONNX — removing the PyTorch runtime dependency from production
3. A FastAPI app loads the ONNX model and serves predictions via a REST endpoint
4. The whole app is packaged into a Docker image

## API

`POST /predict`

```json
{ "text": "Świetny produkt, polecam!" }
```

```json
{ "sentiment": ["positive"] }
```

`GET /health` — liveness check

`GET /docs` — Swagger UI

## Tech Stack

| Layer | Technology |
|-------|-----------|
| API | FastAPI, Pydantic, Uvicorn |
| ML inference | ONNX Runtime, Tokenizers |
| Model source | HuggingFace Transformers |
| Containerization | Docker (multi-stage build) |
| Package manager | uv |
| CI/CD | GitHub Actions |
| Linting | Ruff |
| Security | pip-audit |
| Testing | pytest |

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci_cd_workflow.yaml`) runs two jobs:

**Integration** — runs on every trigger:
- Install dependencies with `uv`
- Lint with `ruff`
- Security audit with `pip-audit`
- Run `pytest`

**Deployment** — builds a production Docker image:
- Download model artifacts from Hugging Face
- Export model to ONNX
- Build lightweight Docker image (ONNX Runtime only, no PyTorch)

## Getting Started

### Run locally

```bash
cd polish-sentiment-app
uv sync --group inference
make prepare_artifacts    # download model from HuggingFace
make export_model_to_onnx
make start                # runs on http://localhost:8000
```

### Run with Docker

```bash
cd polish-sentiment-app
make prepare_artifacts
make export_model_to_onnx
make build_docker
make start_docker         # runs on http://localhost:8000
```

## Project Structure

```
polish-sentiment-app/
├── app.py                  # FastAPI application
├── settings.py             # Configuration (model paths, names)
├── main.py                 # CLI for downloading and exporting the model
├── src/
│   ├── inference/          # ONNX model loading and prediction logic
│   ├── scripts/            # Download from HuggingFace, export to ONNX
│   └── app/                # Pydantic request/response models
├── tests/                  # pytest test suite
├── Dockerfile              # Multi-stage build
├── Makefile                # Developer shortcuts
└── pyproject.toml          # Dependencies (inference / integration / deployment groups)
```
