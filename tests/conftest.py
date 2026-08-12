import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as original_activities


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities state before each test."""
    backup = copy.deepcopy(original_activities)
    try:
        yield
    finally:
        original_activities.clear()
        original_activities.update(backup)


@pytest.fixture
def client():
    """Return a TestClient for the FastAPI app."""
    with TestClient(app) as test_client:
        yield test_client
