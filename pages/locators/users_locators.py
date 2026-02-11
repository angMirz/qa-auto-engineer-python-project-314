from selenium.webdriver.common.by import By


class UsersLocators:
    CREATE_BUTTON = (By.CSS_SELECTOR, "a[aria-label='Create']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "form input[name='email']")
    NAME_INPUT = (By.CSS_SELECTOR, "form input[name='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "form input[name='lastName']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Save']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Delete']")
    ALL_DELETE_BUTTON = (By.CSS_SELECTOR, "th .MuiCheckbox-root.select-all")
    SNACKBAR = (By.CSS_SELECTOR, ".MuiSnackbarContent-message")


    USERS_TABLE = (By.CSS_SELECTOR, "table.RaDatagrid-table")
    USER_ROWS = (By.CSS_SELECTOR, "table.RaDatagrid-table tbody tr")
    TABLE_HEADERS = (By.CSS_SELECTOR, "thead span[data-field]")

    # Ячейки внутри строки
    EMAIL_CELL = ".column-email"
    FIRST_NAME_CELL = ".column-firstName"
    LAST_NAME_CELL = ".column-lastName"

    #Ошибки
    EMAIL_HELPER_TEXT = (By.CSS_SELECTOR,"p.Mui-error")

