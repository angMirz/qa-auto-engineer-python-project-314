# ## Импорт библиотеки для управления браузером
# from selenium import webdriver
# import time

# ## Запуск браузера Chrome через драйвер
# driver = webdriver.Chrome()

# ## Открытие страницы
# driver.get("https://example.com")
# #зависаем на 5сек, чтобы увидеть браузер
# time.sleep(5)

# ## Закрытие браузера и завершение сессии
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_form_elements_exist(base_url):
    # Запуск браузера
    driver = webdriver.Chrome()

    # Открытие приложения
    driver.get(base_url) 
    
    # Проверка: два поля ввода
    inputs = driver.find_elements(By.TAG_NAME, "input")
    assert len(inputs) == 2

    # Проверка кнопки
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert button.is_displayed()

    # Закрытие браузера
    driver.quit()
