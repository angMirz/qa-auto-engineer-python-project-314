from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


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
    
    def type(self, locator, text):
        """Очистка и ввод текста"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        # el.clear()
        # el.send_keys(Keys.CONTROL + "a")
        # el.send_keys(Keys.BACKSPACE) # очистить
        # очистка через JS
        el.click()

        self.driver.execute_script("arguments[0].value = '';", el)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", el)
        import time
        time.sleep(0.1)

        el.send_keys(text)

    def text_of(self, locator):
        """Получение текста элемента"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text

    def value_of(self, locator):
        """Получение значения input-поля"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        # print("DEBUG: найден элемент", el, "tag_name:", el.tag_name)
        # print("DEBUG: value атрибута:", el.get_attribute("value"))
        return el.get_attribute("value")


    def wait_for_snackbar_to_disappear(self, locator):
        el = self.wait.until(EC.invisibility_of_element_located(locator))
        # return el.text  
