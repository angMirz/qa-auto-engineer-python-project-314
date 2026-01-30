from pages.base_page import BasePage
from .locators.users_locators import UsersLocators
from selenium.webdriver.common.by import By
import time

class UsersPage(BasePage):
    CREATE_BUTTON = UsersLocators.CREATE_BUTTON
    NAME_INPUT = UsersLocators.NAME_INPUT
    LASTNAME_INPUT = UsersLocators.LASTNAME_INPUT
    EMAIL_INPUT = UsersLocators.EMAIL_INPUT
    SAVE_BUTTON = UsersLocators.SAVE_BUTTON
    DELETE_BUTTON = UsersLocators.DELETE_BUTTON
    ALL_DELETE_BUTTON = UsersLocators.ALL_DELETE_BUTTON

    SNACKBAR = UsersLocators.SNACKBAR
    USERS_TABLE = UsersLocators.USERS_TABLE     # Таблица со списком пользователей
    USER_ROWS = UsersLocators.USER_ROWS     # Все строки таблицы пользователей
    TABLE_HEADERS = UsersLocators.TABLE_HEADERS
    EMAIL_HELPER_TEXT = UsersLocators.EMAIL_HELPER_TEXT

    def open_users_page(self, base_url):
        """
        Открывает страницу управления пользователями.
        :param base_url: базовый URL приложения
        """
        self.open(f"{base_url}/#/users")

    def create_user(self, first_name, last_name, email):
        self.click(self.CREATE_BUTTON)
        self.fill_and_save_user_form(first_name, last_name, email)

    
    def fill_and_save_user_form(self, first_name, last_name, email):
        """
        Заполняет форму пользователя (создание / редактирование) и сохраняет
        """
        self.type(self.NAME_INPUT, first_name)
        self.type(self.LASTNAME_INPUT, last_name)
        self.type(self.EMAIL_INPUT, email)

        self.click(self.SAVE_BUTTON)
        self.wait_for_snackbar_to_disappear(self.SNACKBAR)
    
    def edit_email_user_form(self, email):
        """
        Очищает и заполняет поле email
        """
        self.type(self.EMAIL_INPUT, email)
        self.click(self.SAVE_BUTTON)

        # self.wait_for_snackbar_to_disappear(self.SNACKBAR)
    
    def email_error_text(self):
        return self.text_of(self.EMAIL_HELPER_TEXT)

    def snackbar_text(self):
        return self.text_of(self.SNACKBAR)



    
    # def create_user(self, first_name, last_name, email):
    #     """
    #     Создаёт нового пользователя через форму на странице.
    #     :param first_name: имя нового пользователя
    #     :param last_name: фамилия нового пользователя
    #     :param email: email нового пользователя
    #     """
    #     self.click(self.CREATE_BUTTON)            # Нажимаем кнопку "Создать"
    #     self.type(self.NAME_INPUT, first_name)    # Вводим имя
    #     self.type(self.LASTNAME_INPUT, last_name) # Вводим фамилию
    #     self.type(self.EMAIL_INPUT, email)      # Вводим email
        
    #     self.click(self.SAVE_BUTTON)              # Нажимаем "Сохранить"
    #     self.wait_for_snackbar_to_disappear(self.SNACKBAR)
    #     # time.sleep(5)
    
    
    def get_table_header_fields(self):
        table = self.driver.find_element(*UsersLocators.USERS_TABLE)
        headers = table.find_elements(*UsersLocators.TABLE_HEADERS)
        return [h.get_attribute("data-field") for h in headers]


    def get_all_users(self):
        """
        Получает список всех пользователей из таблицы.
        :return: список словарей с данными пользователей
        """
        users = []
        rows = self.driver.find_elements(*UsersLocators.USER_ROWS)
        for row in rows:
            email = row.find_element(By.CSS_SELECTOR, UsersLocators.EMAIL_CELL).text
            first_name = row.find_element(By.CSS_SELECTOR, UsersLocators.FIRST_NAME_CELL).text
            last_name = row.find_element(By.CSS_SELECTOR, UsersLocators.LAST_NAME_CELL).text
            users.append({
                "email": email,
                "first_name": first_name,
                "last_name": last_name
            })
        return users

    def open_user_edit_by_email(self, email):
        rows = self.driver.find_elements(*UsersLocators.USER_ROWS)

        for row in rows:
            cell_email = row.find_element(By.CSS_SELECTOR, UsersLocators.EMAIL_CELL).text
            if cell_email == email:
                row.click()
                return

        raise AssertionError(f"Пользователь с email {email} не найден")

    def delete_user_edit_form(self):
        self.click(self.DELETE_BUTTON)

    def all_delete_users_form(self):
        self.click(self.ALL_DELETE_BUTTON)
        self.click(self.DELETE_BUTTON)

    
