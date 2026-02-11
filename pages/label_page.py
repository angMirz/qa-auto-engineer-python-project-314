from selenium.webdriver.common.by import By

from pages.base_table_page import TablePage

from .locators.labels_locators import LabelLocators


class LabelPage(TablePage):
    URL = "labels"

    CREATE_BUTTON = LabelLocators.CREATE_BUTTON
    SAVE_BUTTON = LabelLocators.SAVE_BUTTON
    DELETE_BUTTON = LabelLocators.DELETE_BUTTON
    SNACKBAR = LabelLocators.SNACKBAR

    TABLE = LabelLocators.ST_TABLE
    TABLE_HEADERS = LabelLocators.TABLE_HEADERS
    ROWS = LabelLocators.ST_ROWS

    NAME_INPUT = LabelLocators.NAME_INPUT

    def create_label(self, name):
        self.click_create()
        self.fill_and_save_label_form(name)

    def fill_and_save_label_form(self, name):
        self.type(self.NAME_INPUT, name)
        self.click_save()
        self.wait_snackbar()

    def get_all_label(self):
        labels = []
        for row in self.driver.find_elements(*self.ROWS):
            name = row.find_element(By.CSS_SELECTOR, LabelLocators.NAME_CELL).text
            labels.append({"name": name})
        return labels

    def open_label_edit_by_name(self, name):
        self.open_row_by_cell_value(LabelLocators.NAME_CELL, name)

    def delete_label_edit_form(self):
        self.click_delete()
