from pages.base_page import BasePage
from .locators.tasks_locators import TasksLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaskPage(BasePage):
    URL = "tasks"

    CREATE_BUTTON = TasksLocators.CREATE_BUTTON
    SAVE_BUTTON = TasksLocators.SAVE_BUTTON
    DELETE_BUTTON = TasksLocators.DELETE_BUTTON
    EDIT_BUTTON = TasksLocators.EDIT_BUTTON
    SNACKBAR = TasksLocators.SNACKBAR

    TITLE_INPUT = TasksLocators.TITLE_INPUT
    ASSIGNEE_SELECT = TasksLocators.ASSIGNEE_SELECT
    STATUS_SELECT = TasksLocators.STATUS_SELECT
    LABEL_SELECT = TasksLocators.LABEL_SELECT
    

    def open_page(self, base_url):
        """Открывает страницу по базовому URL + URL класса"""
        self.open(f"{base_url}/#/{self.URL}")


    def create_task(self, title, assigne_value, status_value):
        self.click(self.CREATE_BUTTON)
        self.fill_and_save_task_form(title, assigne_value, status_value)


    def fill_and_save_task_form(self, title, assigne_value, status_value):
        """
        Заполняет форму (создание / редактирование) и сохраняет
        """
        self.type(self.TITLE_INPUT, title)
        self.click(self.ASSIGNEE_SELECT)
        self.select_from_custom_dropdown(self.ASSIGNEE_SELECT, assigne_value)
        self.click(self.STATUS_SELECT)
        self.select_from_custom_dropdown(self.STATUS_SELECT, status_value)

        self.click(self.SAVE_BUTTON)
        self.wait_for_snackbar_to_disappear(self.SNACKBAR)


    def get_all_task(self, status_value: str) -> list[str]:
        titles = self.driver.find_elements(
            By.XPATH,
            f"//h6[normalize-space()='{status_value}']"
            f"/following-sibling::div"
            f"//div[contains(@class,'MuiTypography-h5')]"
        )
        return [t.text for t in titles]


    def snackbar_text(self):
        return self.text_of(self.SNACKBAR)


    def get_tasks_board_state(self) -> dict:
        columns = self.driver.find_elements(By.XPATH, "//h6")
        tasks = self.driver.find_elements(
            By.XPATH, "//div[contains(@class,'MuiTypography-h5')]"
        )

        return {
            "columns": [c.text for c in columns],
            "tasks": [t.text for t in tasks]
        }


    def filters_tasks_board(self, assigne_value, status_value):
        """
        Фильтры
        """
        self.click(self.ASSIGNEE_SELECT)
        self.select_from_custom_dropdown(self.ASSIGNEE_SELECT, assigne_value)
        self.click(self.STATUS_SELECT)
        self.select_from_custom_dropdown(self.STATUS_SELECT, status_value)
        self.click(self.LABEL_SELECT)
        self.click((By.CSS_SELECTOR, "ul[role='listbox'] li[aria-label='Clear value']"))



    def open_task_from_board_by_name(self, title: str):
        task = self.driver.find_element(
            By.XPATH,
            f"//div[contains(@class,'MuiTypography-h5') and contains(., '{title}')]"
        )

        # скроллим карточку в видимую область
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            task
        ) 
            # внутри карточки находим кнопку Edit
        edit_btn = task.find_element(*self.EDIT_BUTTON)
        edit_btn.click()


    def delete_task_edit_form(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.SNACKBAR))
        self.click(self.DELETE_BUTTON)