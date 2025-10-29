"""
Here we declare constants which contains xpath strings to page elements
"""
from enum import Enum
from selenium.webdriver.common.by import By

class HomeElements(Enum):
    JS_DELAYS_BTN = (By.XPATH, "//a[@class=\"wp-block-button__link wp-element-button\" and contains(text(), \"JavaScript Delays\")]")