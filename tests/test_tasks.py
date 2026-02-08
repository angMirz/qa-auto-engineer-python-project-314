import pytest
from pages.tasks_page import TaskPage
from test_data.tasks import TEST_TASK
from test_data.upd_tasks import UPD_TEST_TASK


    # Тест создания задачи
def test_create_task(driver, base_url, logged_in):
    page = TaskPage(driver)
    page.open_page(base_url)

    page.create_task(
        TEST_TASK["title"],
        TEST_TASK["assigne_value"],
        TEST_TASK["status_value"]
        )

    # Проверяем, что задача появилась в списке
    page.open_page(base_url)

    titles = page.get_all_task(TEST_TASK["status_value"])
    assert TEST_TASK["title"] in titles



    # Тест просмотр доски
def test_view_task_list(driver, base_url, logged_in, created_task):
    page = TaskPage(driver)
    page.open_page(base_url)

    # Проверка наличия задач и колонок
    state = page.get_tasks_board_state()
    assert len(state["columns"]) > 0, "Колонки не загрузились"
    assert len(state["tasks"]) > 4, "Задачи не загрузились"

    # Фильтры
    page.filters_tasks_board(
        TEST_TASK["assigne_value"],
        TEST_TASK["status_value"]
        )

    # Находим созданную задачу после фильтров
    titles = page.get_all_task(TEST_TASK["status_value"])
    assert TEST_TASK["title"] in titles



    # Тест на изменения задачи / перемещение в другую колонку по статусу
def test_edit_task_form_prefilled(driver, base_url, created_task):
    page = TaskPage(driver)
    page.open_page(base_url)

    # Открываем форму редактирования 
    page.open_task_from_board_by_name(TEST_TASK["title"])

    page.fill_and_save_task_form(
        UPD_TEST_TASK["title"],
        UPD_TEST_TASK["assigne_value"],
        UPD_TEST_TASK["status_value"]
        )

    # Проверяем , что изменился в общем списке и его статус
    titles = page.get_all_task(UPD_TEST_TASK["status_value"])
    assert UPD_TEST_TASK["title"] in titles


#     # Перетаскивание задачи / не работает из-за react DnD
# def test_drag_and_drop_task(driver, base_url, created_task):
#     page = TaskPage(driver)
#     page.open_task_page(base_url)   

#     page.drag_card_to_column_simple(
#         TEST_TASK["title"],
#         UPD_TEST_TASK["status_value"]
#     )

#     # Проверяем , что изменился в общем списке
#     titles = page.get_all_task(UPD_TEST_TASK["status_value"])
#     assert TEST_TASK["title"] in titles


    # Тест на удаление задачи
def test_delete_task_form(driver, base_url, created_task):
    page = TaskPage(driver)
    page.open_page(base_url)

    # Открываем форму редактирования 
    page.open_task_from_board_by_name(TEST_TASK["title"])
    page.delete_task_edit_form()

    snackbar = WebDriverWait(driver, 5).until(
        lambda d: "Element deleted" in page.snackbar_text()
    )
    assert "Element deleted" in page.snackbar_text()

    titles = page.get_all_task(TEST_TASK["status_value"])
    assert TEST_TASK["title"] not in titles, "Задача не удалена"

