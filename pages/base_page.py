from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class BasePage:
    """Базовый класс со стандартными действиями"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, base_url):
        self.driver.get(base_url)

    
    def click(self, locator):
        """Ожидание кликабельности и клик"""
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()


    def click_js(self, element):
        """Клик по элементу через JavaScript"""
        self.driver.execute_script("arguments[0].click();", element)


    def select_from_custom_dropdown(self, dropdown_locator, value):
        """
        Выбираем элемент из кастомного MUI-дропдауна через JS.
        Работает даже если overlay перекрывает элемент.
        """
        # открыть дропдаун
        dropdown = self.driver.find_element(*dropdown_locator)
        self.click_js(dropdown)

        # найти нужную опцию
        option_locator = (By.XPATH, f"//ul[@role='listbox']//li[normalize-space(.)='{value}']")
        option = self.driver.find_element(*option_locator)

        # клик по опции через JS
        self.click_js(option)

    
    def type(self, locator, text):
        """Очистка и ввод текста"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.click()

        self.driver.execute_script("arguments[0].value = '';", el)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", el)

        el.send_keys(text)


    def text_of(self, locator):
        """Получение текста элемента"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text


    def value_of(self, locator):
        """Получение значения input-поля"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.get_attribute("value")


    def wait_for_snackbar_to_disappear(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
