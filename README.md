### Hexlet tests and linter status:
[![Actions Status](https://github.com/angMirz/qa-auto-engineer-python-project-314/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/angMirz/qa-auto-engineer-python-project-314/actions)

## Project structure
**`/pages/locators/..`** - основные локаторы.
**`/pages/..`**  - основные методы для страниц.
**`/conftest.py`**  - фикстуры для тестов.

**`/tests/test_data/..`** - тестовые данные.
**`/tests/test_login.py`** - тесты на логин/авторизацию.
**`/tests/test_logout.py`** - тесты на логаут.
**`/tests/test_users.py`** - тесты на базовый функционал страницы users.
**`/tests/test_statuses.py`** - тесты на базовый функционал страницы statuses.
**`/tests/test_label.py`** - тесты на базовый функционал страницы label.
**`/tests/test_tasks.py`** - тесты на базовый функционал страницы tasks.

### Usage command
**make start** - старт приложения через докер.
**make stop** -  стоп приложения в докере.
**make test** -   запуск тестов на странице login, users, statuses, labels, tasks(создание/редактирование/поиск/фильтр/удаление).