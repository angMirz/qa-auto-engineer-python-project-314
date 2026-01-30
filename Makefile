.PHONY: start

start:
	docker run --rm -p 5173:5173 hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app

smoke:
	uv run pytest -k smoke

one-login:
	pytest tests/test_login.py::test_login_success_header

two-login:
	pytest tests/test_login.py::test_login_success_url

login:
	pytest tests/test_login.py

logout:
	pytest tests/test_logout.py

users:
	pytest tests/test_users.py

