from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):

    # Локаторы/selectors, которые используются для поиска элементов на странице.
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    HEADER = (By.ID, "react-admin-title")
    PROFILE_BTN = (By.CSS_SELECTOR, "button[aria-label='Profile']")
    LOGOUT_BTN = (
        By.XPATH,
        "//li[@role='menuitem' and .//span[normalize-space()='Logout']]"
    )
    
    # Открывает стартовую страницу, base_url передаётся из фикстуры
    def open(self, base_url):
        """Открывает страницу логина"""
        self.driver.get(base_url)

    def login(self, username, password):
        """Авторизация"""
        self.type(self.USERNAME, username) 
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    # --- Проверка авторизации ---
    # def is_logged_in(self):
    #     """Проверяет, залогинен ли пользователь"""
    #     try:
    #         WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(self.HEADER)
    #         )
    #         return True
    #     except:
    #         return False

    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: "/login" not in d.current_url
            )
            return True
        except TimeoutException:
            return False

    def logout(self):
        """Выход из аккаунта"""
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.PROFILE_BTN)
        ).click()

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.LOGOUT_BTN)
        ).click()

        WebDriverWait(self.driver, 5).until(EC.url_contains("/login"))