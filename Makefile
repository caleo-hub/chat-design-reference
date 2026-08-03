.PHONY: bootstrap check verify run

bootstrap:
	uv sync --all-groups

check:
	uv run ruff check .
	uv run mypy src
	uv run pytest -q

verify: check
	uv run lint-imports

run:
	uv run uvicorn chat_design_reference.api.app:create_app --factory --reload
