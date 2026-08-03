.PHONY: bootstrap check verify run

UV_RUN := uv run --locked

bootstrap:
	uv sync --locked --all-groups

check:
	$(UV_RUN) ruff check .
	$(UV_RUN) mypy src
	$(UV_RUN) pytest -q

verify: check
	$(UV_RUN) lint-imports
	uv build

run:
	$(UV_RUN) uvicorn chat_design_reference.api.app:create_app --factory --reload
