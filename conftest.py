import os, pytest, time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.users_page import UsersPage
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
from tests.test_data.users import TEST_USER

@pytest.fixture(scope="session")
def base_url():
    """Базовый адрес тестируемого сайта"""
    return os.getenv("APP_BASE_URL", "http://localhost:5173")


@pytest.fixture(scope="function")
def driver():
    opts = Options()
    opts.add_argument("--window-size=1366,768")
    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def logged_in(driver, base_url):

    driver.delete_all_cookies()
    page = LoginPage(driver)   
    page.open(base_url)   
    page.login("test", "SecretPassword")
    yield driver

@pytest.fixture
def created_user(driver, logged_in, base_url):
    page = UsersPage(driver)
    page.open_users_page(base_url)
    # time.sleep(5)
    # print("Создаю пользователя...")
    page.create_user(TEST_USER["first_name"], TEST_USER["last_name"], TEST_USER["email"])
    # time.sleep(5)
    # print("Пользователь создан, передаю в тест")
    yield TEST_USER