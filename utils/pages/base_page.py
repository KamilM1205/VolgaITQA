"""
Here we have BasePage class that realize some methods to work with pages.
"""
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import ByType
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    """
    Base class for pages.
    Contains methods to wait elements.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page_by(self, search_param: tuple[ByType, str], wait_time: float = 10):
        """
        Open web page with selenium by clickable object.
        :param search_param: data for search element (search type(XPath, CssSelector, etc.), search query like XPath, CssSelector, etc.).
        :param wait_time: time to wait in seconds.
        :return: Nothing
        """
        element = self.wait_element_clickable(search_param, wait_time)
        element.click()

    def wait_element_clickable(self, search_param: tuple[ByType, str], wait_time: float = 10) -> WebElement:
        """
        Wait for element to be clickable.
        :param search_param: data for search element (search type(XPath, CssSelector, etc.), search query like XPath, CssSelector, etc.).
        :param wait_time: time to wait in seconds.
        :return: WebElement that is clickable.
        """
        element = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(search_param))

        return element

    def wait_element_visible(self, search_param: tuple[ByType, str], wait_time: float = 10) -> WebElement:
        """
        Wait for element to be visible.
        :param search_param: data for search element (search type(XPath, CssSelector, etc.), search query like XPath, CssSelector, etc.).
        :param wait_time: time to wait in seconds.
        :return: WebElement that is visible.
        """
        element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(search_param))

        return element