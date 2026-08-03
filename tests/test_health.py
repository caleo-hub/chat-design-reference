from httpx import ASGITransport, AsyncClient

from chat_design_reference.api.app import create_app
from chat_design_reference.config import Settings


async def _get(path: str, settings: Settings):
    transport = ASGITransport(app=create_app(settings))
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        return await client.get(path)


async def test_liveness_is_independent_from_runtime_dependencies() -> None:
    response = await _get("/health/live", Settings(database_url=""))

    assert response.status_code == 200
    assert response.json()["status"] == "alive"


async def test_readiness_does_not_claim_success_without_persistence() -> None:
    response = await _get("/health/ready", Settings(database_url=""))

    assert response.status_code == 503
    assert response.json()["reason"] == "durable_runtime_not_wired"


async def test_database_url_alone_does_not_make_foundation_ready() -> None:
    response = await _get(
        "/health/ready",
        Settings(database_url="postgresql+asyncpg://example", runtime_wired=False),
    )

    assert response.status_code == 503
