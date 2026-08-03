from dataclasses import dataclass

from chat_design_reference.config import Settings
from chat_design_reference.core.ports import AgentRuntime, Inbox, Outbox, ToolGateway


@dataclass(frozen=True)
class RuntimeComponents:
    """Composition root inputs for a derived project.

    The reference intentionally does not provide fake durable implementations.
    A project must wire PostgreSQL-backed inbox/outbox before reporting readiness.
    """

    settings: Settings
    inbox: Inbox
    outbox: Outbox
    agent_runtime: AgentRuntime
    tool_gateway: ToolGateway
