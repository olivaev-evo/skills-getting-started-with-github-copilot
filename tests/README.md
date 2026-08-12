# Backend Tests

This directory contains pytest tests for the FastAPI backend.

## Run tests

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run tests:

```bash
pytest -q
```

## What is covered

- GET `/activities`
- POST `/activities/{activity_name}/signup`
- DELETE `/activities/{activity_name}/participants`

Each test uses the Arrange-Act-Assert pattern and resets the in-memory activity state between runs.
