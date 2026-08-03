import json
from datetime import UTC, datetime
from pathlib import Path

from jsonschema import Draft202012Validator

from chat_design_reference.core.contracts import (
    ChannelCapabilities,
    ChannelEnvelope,
    ContentKind,
    ContentPart,
    MessageDirection,
)


ROOT = Path(__file__).resolve().parents[1]


def _envelope() -> ChannelEnvelope:
    return ChannelEnvelope(
        event_id="evt-1",
        provider_message_id="provider-1",
        tenant_id="tenant-1",
        channel="web",
        channel_account_id="web-main",
        conversation_id="conversation-1",
        participant_id="participant-1",
        direction=MessageDirection.INBOUND,
        received_at=datetime.now(UTC),
        correlation_id="corr-1",
        content=[ContentPart(kind=ContentKind.TEXT, text="Olá")],
        capabilities=ChannelCapabilities(streaming=True, typing=True),
    )


def test_channel_envelope_matches_json_schema() -> None:
    schema = json.loads((ROOT / "contracts/channel-envelope.schema.json").read_text())
    validator = Draft202012Validator(
        schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
    validator.validate(_envelope().model_dump(mode="json"))


def test_contract_json_files_are_valid_json() -> None:
    for path in (ROOT / "contracts").glob("*.json"):
        parsed = json.loads(path.read_text())
        assert parsed["$schema"] == "https://json-schema.org/draft/2020-12/schema"
