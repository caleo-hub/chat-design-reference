from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import datetime
from typing import Any, Protocol

from chat_design_reference.core.contracts import (
    ChannelEnvelope,
    OutboundMessage,
    ToolResult,
    TurnRequest,
    TurnResult,
)


class Inbox(Protocol):
    async def enqueue(self, envelope: ChannelEnvelope) -> tuple[str, bool]:
        """Return receipt ID and whether this was a duplicate."""
        ...


class AgentRuntime(Protocol):
    async def execute(self, request: TurnRequest) -> TurnResult: ...


class ToolGateway(Protocol):
    async def call(
        self,
        *,
        tool_name: str,
        arguments: Mapping[str, Any],
        scopes: Sequence[str],
        correlation_id: str,
        idempotency_key: str | None = None,
        deadline_at: datetime | None = None,
    ) -> ToolResult: ...


class Outbox(Protocol):
    async def append(self, message: OutboundMessage) -> str: ...


class ChannelSender(Protocol):
    async def send(self, message: OutboundMessage) -> str: ...


class Clock(Protocol):
    def now(self) -> datetime: ...
