"""
Here we initialize selenium and PyTest
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Select webdriver: chrome or firefox."
    )

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def initialize_browser(request, browser):
    """
    Initialize selenium webdriver
    :param request: pytest's FixtureRequest object
    :param browser: selected browser name(firefox or chrome)
    :return: webdriver
    """
    driver = None
    options = Options()

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    def deinit_browser():
        driver.quit()
    request.addfinalizer(deinit_browser)

    driver.navigate().to("https://practice-automation.com/")

    return driver