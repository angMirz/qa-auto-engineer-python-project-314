# import pytest
# from selenium.webdriver.common.by import By


# def test_logout_redirect_to_login(logged_in):
#     driver = logged_in

#     driver.find_element(By.CSS_SELECTOR, "button[aria-label='Profile']").click()
#     # Нажимаем кнопку выхода
#     driver.find_element(
#         By.XPATH, "//li[@role='menuitem' and .//span[normalize-space()='Logout']]"
#         ).click()
    
#     # Проверяем, что в URL есть "/login"
#     assert "/login" in driver.current_url

# from selenium.webdriver.common.by import By

# from pages.login_page import LoginPage
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait


def test_logout_redirect_to_login(logged_in):
    page = logged_in
    page.logout()

    assert "/login" in page.driver.current_url


# def test_logout_redirect_to_login(logged_in):
#     driver = logged_in

#     print("Текущий URL до клика по профилю:", driver.current_url)

#     # Ждём кнопку профиля
#     try:
#         profile_btn = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable(
#                 (By.CSS_SELECTOR, "button[aria-label='Profile']")
#                 )
#         )
#         print("Кнопка профиля найдена:", profile_btn)
#         profile_btn.click()
#     except Exception as e:
#         print("Не удалось найти или кликнуть кнопку профиля:", e)
#         raise

#     # Ждём кнопку Logout
#     try:
#         logout_btn = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable(
#                 (
#                     By.XPATH,
#                     "//li[@role='menuitem' and "
#                     ".//span[normalize-space()='Logout']]"
#                 )
#             )
#         )

#         print("Кнопка Logout найдена:", logout_btn.text)
#         logout_btn.click()
#     except Exception as e:
#         print("Не удалось найти или кликнуть кнопку Logout:", e)
#         raise

#     # Ждём редирект на /login
#     try:
#         WebDriverWait(driver, 5).until(EC.url_contains("/login"))
#         print("Редирект на /login произошёл, текущий URL:", driver.current_url)
#     except Exception as e:
#         print("Редирект на /login не произошёл, текущий URL:", driver.current_url, e)
#         raise

#     assert "/login" in driver.current_url
