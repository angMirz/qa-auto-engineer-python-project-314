from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

# def test_login_success_url(logged_in):
#     page = logged_in
#     assert "/login" not in page.driver.current_url
    
def test_login_success(logged_in):
    page = logged_in
    assert page.is_logged_in()

def test_login_success_header(logged_in):
    page = logged_in
    # Находим заголовок по ID
    header = page.driver.find_element(By.ID, "react-admin-title")
    assert "Welcome to the administration" in header.text


def test_login_fail_empty_fields(driver, base_url):
    page = LoginPage(driver)
    page.open(base_url)

    page.login("", "")

    # Должны остаться на странице логина
    assert "/login" in driver.current_url
