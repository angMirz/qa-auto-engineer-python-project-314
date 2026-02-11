from selenium.webdriver.support.ui import WebDriverWait
from pages.label_page import LabelPage
from test_data.label import TEST_LABEL
from test_data.upd_label import UPD_TEST_LABEL


    # Тест создания метки
def test_create_label(driver, base_url, logged_in):
    page = LabelPage(driver)
    page.open_page(base_url)

    page.create_label(
        TEST_LABEL["name"]
        )

    # Проверяем, что метка появилась в списке
    page.open_page(base_url)

    status = page.get_all_label()
    assert any(u["name"] == TEST_LABEL["name"] for u in status), "Метка не найдена"


    # Тест просмотр списка
def test_view_label_list(driver, base_url, logged_in):
    page = LabelPage(driver)
    page.open_page(base_url)

    # Проверка ключевых полей в заголовке(шапке)
    headers = page.get_table_header_fields()
    assert "name" in headers

    # Проверка ключевых полей в строках
    status = page.get_all_label()
    for u in status:
        assert u["name"], "Название метки отсутствует"


    # Тест на изменения метки
def test_edit_label_form_prefilled(driver, base_url, created_label):
    page = LabelPage(driver)
    page.open_page(base_url)

    # Открываем форму редактирования 
    page.open_label_edit_by_name(TEST_LABEL["name"])

    page.fill_and_save_label_form(
        UPD_TEST_LABEL["name"]
        )

    # Проверяем , что изменился в общем списка
    status = page.get_all_label()
    assert any(u["name"] == UPD_TEST_LABEL["name"] for u in status)



    # Тест на удаление метки
def test_delete_label_form(driver, base_url, created_label):
    page = LabelPage(driver)

    page.delete_label_edit_form()

    WebDriverWait(driver, 5).until(
        lambda d: "Element deleted" in page.snackbar_text()
    )
    assert "Element deleted" in page.snackbar_text()

    status = page.get_all_label()
    assert not any(u["name"] == TEST_LABEL["name"] for u in status), "Метка не удалена"

