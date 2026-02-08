from pages.base_table_page import TablePage
from .locators.users_locators import UsersLocators
from selenium.webdriver.common.by import By

class UsersPage(TablePage):
    URL = "users"

    CREATE_BUTTON = UsersLocators.CREATE_BUTTON
    SAVE_BUTTON = UsersLocators.SAVE_BUTTON
    DELETE_BUTTON = UsersLocators.DELETE_BUTTON
    ALL_DELETE_BUTTON = UsersLocators.ALL_DELETE_BUTTON
    SNACKBAR = UsersLocators.SNACKBAR

    TABLE = UsersLocators.USERS_TABLE
    TABLE_HEADERS = UsersLocators.TABLE_HEADERS
    ROWS = UsersLocators.USER_ROWS

    NAME_INPUT = UsersLocators.NAME_INPUT
    LASTNAME_INPUT = UsersLocators.LASTNAME_INPUT
    EMAIL_INPUT = UsersLocators.EMAIL_INPUT
    EMAIL_HELPER_TEXT = UsersLocators.EMAIL_HELPER_TEXT

    # CRUD
    def create_user(self, first_name, last_name, email):
        self.click_create()
        self.fill_and_save_user_form(first_name, last_name, email)

    def fill_and_save_user_form(self, first_name, last_name, email):
        self.type(self.NAME_INPUT, first_name)
        self.type(self.LASTNAME_INPUT, last_name)
        self.type(self.EMAIL_INPUT, email)
        self.click_save()
        self.wait_snackbar()

    def edit_email_user_form(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.click_save()

    def email_error_text(self):
        return self.text_of(self.EMAIL_HELPER_TEXT)

    def get_all_users(self):
        users = []
        for row in self.driver.find_elements(*self.ROWS):
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
        self.open_row_by_cell_value(UsersLocators.EMAIL_CELL, email)

    def delete_user_edit_form(self):
        self.click_delete()

    def all_delete_users_form(self):
        # твой старый метод "удалить всех пользователей"
        self.click(self.ALL_DELETE_BUTTON)
        self.click_delete()