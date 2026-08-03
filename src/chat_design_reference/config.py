from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_env: str = "local"
    app_name: str = "chat-design-reference"
    app_host: str = "0.0.0.0"
    app_port: int = Field(default=8000, ge=1, le=65535)
    log_level: str = "INFO"
    database_url: str = ""
    runtime_wired: bool = False
    agent_runtime: str = "stub"
    mcp_enabled: bool = False
    queue_lease_seconds: int = Field(default=120, ge=10)
    heartbeat_interval_seconds: int = Field(default=15, ge=1)
    nudge_after_seconds: int = Field(default=15, ge=0)
    turn_timeout_seconds: int = Field(default=90, ge=1)

    @property
    def is_runtime_wired(self) -> bool:
        """Foundation gate, not a replacement for dependency probes.

        A derived project must wire PostgreSQL-backed inbox/outbox and replace
        readiness with real checks before enabling this flag.
        """
        return self.runtime_wired and bool(self.database_url.strip())


@lru_cache
def get_settings() -> Settings:
    return Settings()
