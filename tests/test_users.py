import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.users_page import UsersPage
from test_data.users import TEST_USER 
from test_data.upd_users import UPD_TEST_USER


# Тест создания пользователя
def test_create_user(driver, base_url, logged_in):
    page = UsersPage(driver)
    page.open_page(base_url)

    page.create_user(
        TEST_USER["first_name"],
        TEST_USER["last_name"],
        TEST_USER["email"]
        )

    # Проверяем, что пользователь появился в списке
    page.open_page(base_url)

    users = page.get_all_users()
    assert any(u["email"] == TEST_USER["email"] for u in users), "Пользователь не найден в списке!"


# Тест полей пользователя появился в списке
def test_view_users_list(driver, base_url, logged_in):
    page = UsersPage(driver)
    page.open_page(base_url)

    headers = page.get_table_header_fields()
    # Проверка ключевых полей в заголовке(шапке)
    assert "email" in headers
    assert "firstName" in headers
    assert "lastName" in headers

    users = page.get_all_users()
    assert len(users) > 0, "Список пользователей пуст!"
    # Проверка ключевых полей в строках
    for u in users:
        assert u["first_name"], "Имя пользователя отсутствует"
        assert u["last_name"], "Фамилия пользователя отсутствует"
        assert u["email"], "Email пользователя отсутствует"


# Тест на валидацию и изменения пользователя
def test_edit_user_form_prefilled(driver, base_url, created_user):
    page = UsersPage(driver)
    page.open_page(base_url)

    # Открываем форму редактирования созданного пользователя
    page.open_user_edit_by_email(TEST_USER["email"])

    # Проверяем, что поля формы заполнены верно
    assert page.value_of(UsersPage.EMAIL_INPUT) == TEST_USER["email"]
    assert page.value_of(UsersPage.NAME_INPUT) == TEST_USER["first_name"]
    assert page.value_of(UsersPage.LASTNAME_INPUT) == TEST_USER["last_name"]


    page.edit_email_user_form("invalid-email")
    # Проверяем валидацию поля email
    assert "Incorrect email format" in page.email_error_text()

    snackbar_text = page.snackbar_text()
    assert "The form is not valid" in snackbar_text

    page.fill_and_save_user_form(
        UPD_TEST_USER["first_name"],
        UPD_TEST_USER["last_name"],
        UPD_TEST_USER["email"]
        )

    users = page.get_all_users()
    # Проверяем, что поле email изменился в общем списке
    assert any(u["email"] == UPD_TEST_USER["email"] for u in users)


# Тест на удаление пользователя
def test_delete_user_form(driver, base_url, created_user):
    page = UsersPage(driver)

    page.delete_user_edit_form()

    snackbar = WebDriverWait(driver, 5).until(
        lambda d: "Element deleted" in page.snackbar_text()
    )
    assert "Element deleted" in page.snackbar_text()

    users = page.get_all_users()
    assert not any(u["email"] == TEST_USER["email"] for u in users), "Пользователь не удален"


# Тест на удаление всех пользователей
def test_delete_all_users(driver, base_url, logged_in):
    page = UsersPage(driver)
    page.open_page(base_url)

    page.all_delete_users_form()

    snackbar = WebDriverWait(driver, 5).until(
        lambda d: "elements deleted" in page.snackbar_text()
    )
    assert "elements deleted" in page.snackbar_text()

    users = page.get_all_users()
    assert len(users) == 0, "Список не пуст"

    #Негатив
    # try:
    #     page.all_delete_users_form()
    #     snackbar = page.snackbar_text()
    #     assert "elements deleted" in snackbar, "Негативный кейс: список уже пуст"
    # except Exception as e:
    #     raise AssertionError("Негативный кейс: список пуст, удалять нечего") from e
    users = page.get_all_users()
    if not users:
        print("Негативный кейс: список пуст, повторное удаление пропущено")
    else:
        page.all_delete_users_form()
        snackbar = page.snackbar_text()
        assert "elements deleted" in snackbar, "Негативный кейс: элементы должны быть удалены"