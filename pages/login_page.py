from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # Локаторы/selectors, которые используются для поиска элементов на странице.
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    # FLASH = (By.ID, "flash")
    
    # Открывает стартовую страницу, base_url передаётся из фикстуры
    def open(self, base_url):
        """Открывает страницу логина"""
        self.driver.get(base_url)

    def login(self, username, password):
        """Авторизация"""
        # означает: Selenium найдёт элемент с name="username" и введёт туда username.
        # Последовательность действий для логина : сначала имя, пароль и кнопка
        self.type(self.USERNAME, username) 
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    # def message(self):
    #     """Возвращает текст баннера"""
    #     return self.text_of(self.FLASH)