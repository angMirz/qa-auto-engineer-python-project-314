.PHONY: install start stop test

install:
	uv sync

# Запуск приложения
start:
	docker run --rm --name hexlet-app -p 5173:5173 hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app

# Остановка приложения
stop:
	docker stop hexlet-app

# Запуск тестов
test:
	uv run pytest