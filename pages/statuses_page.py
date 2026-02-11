from selenium.webdriver.common.by import By

from pages.base_table_page import TablePage

from .locators.statuses_locators import StatusLocators


class StatusPage(TablePage):
    URL = "task_statuses"

    CREATE_BUTTON = StatusLocators.CREATE_BUTTON
    SAVE_BUTTON = StatusLocators.SAVE_BUTTON
    DELETE_BUTTON = StatusLocators.DELETE_BUTTON
    ALL_DELETE_BUTTON = StatusLocators.ALL_DELETE_BUTTON
    SNACKBAR = StatusLocators.SNACKBAR

    TABLE = StatusLocators.ST_TABLE
    TABLE_HEADERS = StatusLocators.TABLE_HEADERS
    ROWS = StatusLocators.ST_ROWS

    NAME_INPUT = StatusLocators.NAME_INPUT
    SLUG_INPUT = StatusLocators.SLUG_INPUT

    def create_status(self, name, slug):
        self.click_create()
        self.fill_and_save_status_form(name, slug)

    def fill_and_save_status_form(self, name, slug):
        self.type(self.NAME_INPUT, name)
        self.type(self.SLUG_INPUT, slug)
        self.click_save()
        self.wait_snackbar()

    def get_all_statuses(self):
        status = []
        for row in self.driver.find_elements(*self.ROWS):
            name = row.find_element(By.CSS_SELECTOR, StatusLocators.NAME_CELL).text
            slug = row.find_element(By.CSS_SELECTOR, StatusLocators.SLUG_CELL).text
            status.append({"name": name, "slug": slug})
        return status

    def open_status_edit_by_slug(self, slug):
        self.open_row_by_cell_value(StatusLocators.SLUG_CELL, slug)

    def delete_status_edit_form(self):
        self.click_delete()

    def all_delete_status_form(self):
        self.click(self.ALL_DELETE_BUTTON)
        self.click_delete()
