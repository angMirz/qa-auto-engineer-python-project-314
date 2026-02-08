from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # Локаторы/selectors, которые используются для поиска элементов на странице.
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    
    # Открывает стартовую страницу, base_url передаётся из фикстуры
    def open(self, base_url):
        """Открывает страницу логина"""
        self.driver.get(base_url)

    def login(self, username, password):
        """Авторизация"""
        self.type(self.USERNAME, username) 
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)