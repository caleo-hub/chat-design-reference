from fastapi import FastAPI
from fastapi.responses import JSONResponse

from chat_design_reference import __version__
from chat_design_reference.config import Settings, get_settings


def create_app(settings: Settings | None = None) -> FastAPI:
    resolved = settings or get_settings()
    app = FastAPI(
        title="Chat Design Reference",
        version=__version__,
        description=(
            "Foundation harness. The durable webhook/worker/outbox vertical slice "
            "is intentionally not wired yet."
        ),
    )

    @app.get("/")
    def index() -> dict[str, str]:
        return {
            "name": resolved.app_name,
            "version": __version__,
            "architecture": "docs/architecture/index.md",
        }

    @app.get("/health/live")
    def liveness() -> dict[str, str]:
        return {
            "status": "alive",
            "service": resolved.app_name,
            "version": __version__,
        }

    @app.get("/health/ready")
    def readiness() -> JSONResponse:
        if resolved.is_runtime_wired:
            return JSONResponse(
                status_code=200,
                content={
                    "status": "ready",
                    "service": resolved.app_name,
                    "version": __version__,
                },
            )
        return JSONResponse(
            status_code=503,
            content={
                "status": "not_ready",
                "service": resolved.app_name,
                "version": __version__,
                "reason": "durable_runtime_not_wired",
            },
        )

    return app
