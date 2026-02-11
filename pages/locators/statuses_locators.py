from selenium.webdriver.common.by import By


class StatusLocators:
    CREATE_BUTTON = (By.CSS_SELECTOR, "a[aria-label='Create']")
    NAME_INPUT = (By.CSS_SELECTOR, "form input[name='name']")
    SLUG_INPUT = (By.CSS_SELECTOR, "form input[name='slug']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Save']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Delete']")
    ALL_DELETE_BUTTON = (By.CSS_SELECTOR, "th .MuiCheckbox-root.select-all")
    SNACKBAR = (By.CSS_SELECTOR, ".MuiSnackbarContent-message")


    ST_TABLE = (By.CSS_SELECTOR, "table.RaDatagrid-table")
    ST_ROWS = (By.CSS_SELECTOR, "table.RaDatagrid-table tbody tr")
    TABLE_HEADERS = (By.CSS_SELECTOR, "thead span[data-field]")

    # Ячейки внутри строки
    NAME_CELL = ".column-name"
    SLUG_CELL = ".column-slug"


