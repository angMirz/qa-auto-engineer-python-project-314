import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.statuses_page import StatusPage
from test_data.statuses import TEST_STATUS
from test_data.upd_statuses import UPD_TEST_STATUS


    # Тест создания статуса
def test_create_status(driver, base_url, logged_in):
    page = StatusPage(driver)
    page.open_page(base_url)

    page.create_status(
        TEST_STATUS["name"],
        TEST_STATUS["slug"]
        )

    # Проверяем, что статус появился в списке
    page.open_page(base_url)

    status = page.get_all_statuses()
    assert any(u["slug"] == TEST_STATUS["slug"] for u in status), "Статус не найден"


    # Тест просмотр списка
def test_view_status_list(driver, base_url, logged_in):
    page = StatusPage(driver)
    page.open_page(base_url)

    status = page.get_all_statuses()
    assert len(status) > 0, "Список статусов пуст!"

    # Проверка ключевых полей в заголовке(шапке)
    headers = page.get_table_header_fields()
    assert "name" in headers
    assert "slug" in headers

    # Проверка ключевых полей в строках
    for u in status:
        assert u["name"], "Название статуса отсутствует"
        assert u["slug"], "Слаг отсутствует"


    # Тест на изменения статуса
def test_edit_status_form_prefilled(driver, base_url, created_status):
    page = StatusPage(driver)
    page.open_page(base_url)

    # Открываем форму редактирования 
    page.open_status_edit_by_slug(TEST_STATUS["slug"])

    page.fill_and_save_status_form(
        UPD_TEST_STATUS["name"],
        UPD_TEST_STATUS["slug"]
        )

    # Проверяем , что изменился в общем списка
    status = page.get_all_statuses()
    assert any(u["slug"] == UPD_TEST_STATUS["slug"] for u in status)



    # Тест на удаление статуса
def test_delete_status_form(driver, base_url, created_status):
    page = StatusPage(driver)

    page.delete_status_edit_form()

    snackbar = WebDriverWait(driver, 5).until(
        lambda d: "Element deleted" in page.snackbar_text()
    )
    assert "Element deleted" in page.snackbar_text()

    status = page.get_all_statuses()
    assert not any(u["slug"] == TEST_STATUS["slug"] for u in status), "Статус не удален"


    # Тест на удаление всех статусов
def test_delete_all_status(driver, base_url, logged_in):
    page = StatusPage(driver)
    page.open_page(base_url)

    page.all_delete_status_form()

    snackbar = WebDriverWait(driver, 5).until(
        lambda d: "elements deleted" in page.snackbar_text()
    )
    assert "elements deleted" in page.snackbar_text()

    status = page.get_all_statuses()
    assert len(status) == 0, "Список не пуст"