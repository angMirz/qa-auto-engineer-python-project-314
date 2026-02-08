from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_login_success_url(logged_in):
    driver = logged_in
    assert "/login" not in driver.current_url
    

def test_login_success_header(logged_in):
    driver = logged_in
    # Находим заголовок по ID
    header = driver.find_element(By.ID, "react-admin-title")
    assert "Welcome to the administration" in header.text