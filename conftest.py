import os, pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.users_page import UsersPage
from pages.statuses_page import StatusPage
from pages.label_page import LabelPage
from pages.tasks_page import TaskPage
from selenium.webdriver.chrome.options import Options
from tests.test_data.users import TEST_USER
from tests.test_data.statuses import TEST_STATUS
from tests.test_data.label import TEST_LABEL
from tests.test_data.tasks import TEST_TASK

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
    page.open_page(base_url)
    page.create_user(TEST_USER["first_name"], TEST_USER["last_name"], TEST_USER["email"])

    yield TEST_USER


@pytest.fixture
def created_status(driver, logged_in, base_url):
    page = StatusPage(driver)
    page.open_page(base_url)
    page.create_status(TEST_STATUS["name"], TEST_STATUS["slug"])

    yield TEST_STATUS


@pytest.fixture
def created_label(driver, logged_in, base_url):
    page = LabelPage(driver)
    page.open_page(base_url)
    page.create_label(TEST_LABEL["name"])

    yield TEST_LABEL


@pytest.fixture
def created_task(driver, logged_in, base_url):
    page = TaskPage(driver)
    page.open_page(base_url)
    page.create_task(
        TEST_TASK["title"],
        TEST_TASK["assigne_value"],
        TEST_TASK["status_value"]
        )

    yield TEST_TASK