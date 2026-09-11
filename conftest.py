import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер для запуска тестов: chrome или firefox"
    )
    parser.addoption(
        "--url",
        action="store",
        default="https://www.saucedemo.com/",
        help="URL тестируемого сайта"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()