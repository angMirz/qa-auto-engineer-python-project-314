from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TablePage(BasePage):
    """
    Базовый Page Object для страниц с таблицами CRUD (Users, Labels, Statuses)
    Содержит общие методы: открыть строку, кликнуть создать, сохранить, удалить, дождаться snackbar
    """

    CREATE_BUTTON = None
    SAVE_BUTTON = None
    DELETE_BUTTON = None
    SNACKBAR = None

    TABLE = None
    TABLE_HEADERS = None
    ROWS = None

    NAME_INPUT = None  # для Label/Status/User
    LASTNAME_INPUT = None
    EMAIL_INPUT = None
    EMAIL_HELPER_TEXT = None
    SLUG_INPUT = None

    URL = None

    # --- Общие действия ---
    def open_page(self, base_url):
        """Открывает страницу по базовому URL + URL класса"""
        self.open(f"{base_url}/#/{self.URL}")

    def click_create(self):
        """Клик по кнопке создания записи"""
        self.click(self.CREATE_BUTTON)

    def click_save(self):
        """Клик по кнопке сохранить"""
        self.click(self.SAVE_BUTTON)

    def click_delete(self):
        """Клик по кнопке удалить"""
        self.click(self.DELETE_BUTTON)

    def wait_snackbar(self):
        """Ждем пока snackbar появится и исчезнет"""
        self.wait_for_snackbar_to_disappear(self.SNACKBAR)
    
    def snackbar_text(self) -> str:
        """Возвращает текст видимого Snackbar"""
        return self.text_of(self.SNACKBAR)

    def open_row_by_cell_value(self, cell_locator, value):
        """Открывает редактирование строки по значению ячейки"""
        for row in self.driver.find_elements(*self.ROWS):
            cell_text = row.find_element(By.CSS_SELECTOR, cell_locator).text
            if cell_text == value:
                row.click()
                return
        raise AssertionError(f"Значение {value} в таблице не найдено")

    def get_table_header_fields(self) -> list[str]:
        """
        Возвращает список имён колонок таблицы.
        Использует локаторы TABLE и TABLE_HEADERS.
        """
        table = self.driver.find_element(*self.TABLE)
        headers = table.find_elements(*self.TABLE_HEADERS)
        return [h.get_attribute("data-field") for h in headers]
