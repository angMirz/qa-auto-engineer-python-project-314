.PHONY: start

start:
	docker run --rm -p 5173:5173 hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app

active:
	source .venv/bin/activate

smoke:
	uv run pytest -k smoke

one_login:
	pytest tests/test_login.py::test_login_success_header

two_login:
	pytest tests/test_login.py::test_login_success_url

login:
	pytest tests/test_login.py

logout:
	pytest tests/test_logout.py

users:
	pytest tests/test_users.py

statuses:
	pytest tests/test_statuses.py

labels:
	pytest tests/test_labels.py

tasks:
	pytest tests/test_tasks.py

tasks_filters:
	pytest tests/test_tasks.py::test_view_task_list

