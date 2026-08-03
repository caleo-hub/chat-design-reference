from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any, Literal

from pydantic import BaseModel, Field


class MessageDirection(StrEnum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"
    SYSTEM = "system"


class ContentKind(StrEnum):
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    FILE = "file"
    LOCATION = "location"
    INTERACTIVE = "interactive"


class JobStatus(StrEnum):
    QUEUED = "queued"
    PROCESSING = "processing"
    WAITING_TOOL = "waiting_tool"
    WAITING_HUMAN = "waiting_human"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    RECONCILIATION_REQUIRED = "reconciliation_required"


class ToolResultStatus(StrEnum):
    SUCCEEDED = "succeeded"
    NOT_FOUND = "not_found"
    NEEDS_USER_INPUT = "needs_user_input"
    NEEDS_HUMAN = "needs_human"
    REJECTED = "rejected"
    RETRYABLE_ERROR = "retryable_error"
    PERMANENT_ERROR = "permanent_error"
    OUTCOME_UNKNOWN = "outcome_unknown"


class ContentPart(BaseModel):
    kind: ContentKind
    text: str | None = None
    url: str | None = None
    mime_type: str | None = None
    name: str | None = None
    size_bytes: int | None = Field(default=None, ge=0)
    sha256: str | None = Field(default=None, pattern=r"^[a-fA-F0-9]{64}$")
    metadata: dict[str, Any] = Field(default_factory=dict)


class ChannelCapabilities(BaseModel):
    streaming: bool = False
    typing: bool = False
    buttons: bool = False
    message_edit: bool = False
    delivery_events: bool = False
    read_events: bool = False
    max_text_length: int | None = Field(default=None, ge=1)


class ChannelEnvelope(BaseModel):
    schema_version: Literal[1] = 1
    event_id: str = Field(min_length=1, max_length=200)
    provider_message_id: str | None = Field(default=None, max_length=300)
    tenant_id: str = Field(min_length=1, max_length=100)
    channel: str = Field(min_length=1, max_length=50)
    channel_account_id: str = Field(min_length=1, max_length=200)
    conversation_id: str = Field(min_length=1, max_length=300)
    participant_id: str = Field(min_length=1, max_length=300)
    direction: MessageDirection
    received_at: datetime
    correlation_id: str = Field(min_length=1, max_length=100)
    reply_to: str | None = Field(default=None, max_length=300)
    content: list[ContentPart] = Field(min_length=1, max_length=20)
    capabilities: ChannelCapabilities = Field(default_factory=ChannelCapabilities)
    metadata: dict[str, Any] = Field(default_factory=dict)


class OutboundMessage(BaseModel):
    tenant_id: str
    channel: str
    channel_account_id: str
    conversation_id: str
    recipient_id: str
    correlation_id: str
    delivery_key: str
    content: list[ContentPart] = Field(min_length=1)
    metadata: dict[str, Any] = Field(default_factory=dict)


class TurnRequest(BaseModel):
    turn_id: str
    conversation_id: str
    tenant_id: str
    correlation_id: str
    current_message: ChannelEnvelope
    state: dict[str, Any] = Field(default_factory=dict)
    context: dict[str, Any] = Field(default_factory=dict)
    allowed_tool_scopes: list[str] = Field(default_factory=list)
    deadline_at: datetime | None = None
    release_context: dict[str, str] = Field(default_factory=dict)


class TurnResult(BaseModel):
    response: OutboundMessage | None = None
    state_patch: dict[str, Any] = Field(default_factory=dict)
    signals: dict[str, Any] = Field(default_factory=dict)
    handoff_required: bool = False
    final: bool = True


class ToolResult(BaseModel):
    schema_version: Literal[1] = 1
    call_id: str
    tool_name: str
    status: ToolResultStatus
    idempotency_key: str | None = None
    data: dict[str, Any] = Field(default_factory=dict)
    public_message: str | None = None
    error_code: str | None = None
    retry_after_seconds: float | None = Field(default=None, ge=0)
    effect_reference: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
