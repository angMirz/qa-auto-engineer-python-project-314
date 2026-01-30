import pytest
from selenium.webdriver.common.by import By


def test_logout_redirect_to_login(logged_in):
    driver = logged_in

    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Profile']").click()
    # Нажимаем кнопку выхода
    driver.find_element(By.XPATH, "//li[@role='menuitem' and .//span[normalize-space()='Logout']]").click()
    
    # Проверяем, что в URL есть "/login"
    assert "/login" in driver.current_url