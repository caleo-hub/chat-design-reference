from fastapi.testclient import TestClient

from chat_design_reference.api.app import create_app
from chat_design_reference.config import Settings


def test_liveness_is_independent_from_runtime_dependencies() -> None:
    client = TestClient(create_app(Settings(database_url="")))

    response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json()["status"] == "alive"


def test_readiness_does_not_claim_success_without_persistence() -> None:
    client = TestClient(create_app(Settings(database_url="")))

    response = client.get("/health/ready")

    assert response.status_code == 503
    assert response.json()["reason"] == "persistence_not_configured"
