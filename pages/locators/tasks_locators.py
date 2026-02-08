from selenium.webdriver.common.by import By

class TasksLocators:
    CREATE_BUTTON = (By.CSS_SELECTOR, "a[aria-label='Create']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Save']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Delete']")
    EDIT_BUTTON = (By.XPATH, "//div[contains(@class,'MuiCard-root') and .//div[contains(@class,'MuiTypography-h5') and text()='Test']]//a[@aria-label='Edit']")
    SNACKBAR = (By.CSS_SELECTOR, ".MuiSnackbarContent-message")

    TITLE_INPUT = (By.CSS_SELECTOR, "form input[name='title']")
    ASSIGNEE_SELECT = (By.CSS_SELECTOR, "div.ra-input-assignee_id div[role='combobox']")
    STATUS_SELECT = (By.CSS_SELECTOR, "div.ra-input-status_id div[role='combobox']")
    LABEL_SELECT = (By.CSS_SELECTOR, "div.ra-input-label_id div[role='combobox']")



