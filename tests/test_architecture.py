import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "src" / "chat_design_reference" / "core"
FORBIDDEN_PREFIXES = (
    "fastapi",
    "sqlalchemy",
    "langchain",
    "langgraph",
    "crewai",
    "mcp",
    "chat_design_reference.api",
)


def _imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(), filename=str(path))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
    return names


def test_core_does_not_import_framework_or_adapter_modules() -> None:
    violations: list[str] = []
    for path in ROOT.rglob("*.py"):
        for imported in _imports(path):
            if imported.startswith(FORBIDDEN_PREFIXES):
                violations.append(f"{path.relative_to(ROOT)} imports {imported}")
    assert not violations, "\n".join(violations)
