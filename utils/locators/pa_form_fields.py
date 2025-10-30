from enum import Enum

from selenium.webdriver.common.by import By


class FormFieldsCheckbox:
    """
    That class uses for represent checkboxes in form fields page
    """
    checkbox_path: str
    title_path: str
    title: str

    def __init__(self, element_id: int, title:str):
        """
        Initialize form field page checkbox element
        :param element_id: Since we have checkboxes ids like "drinkN", where N is drink number we can optimize xpath contain.
        :param title: checkbox title
        """
        self.checkbox_path = format("//input[@id=\"drink{id}\"]", str(element_id))
        self.title_path = format("//label[@for=\"drink{}\"]", str(element_id))
        self.title = title


class FormFieldsRadiobutton:
    """
    That class uses for represent radiobuttons in form fields page
    """
    radiobutton_path: str
    title_path: str
    title: str

    def __init__(self, element_id: int, title:str):
        """
        Initialize form field page radiobutton element
        :param element_id: Since we have radiobuttons ids like "colorN", where N is color number we can optimize xpath contain.
        :param title: radiobutton title
        """
        self.checkbox_path = format("//input[@id=\"color{}\"]", str(element_id))
        self.title_path = format("//label[@for=\"color{}\"]", str(element_id))
        self.title = title


class FormFieldsTextListItem:
    """
    That class uses for represent text list item in form fields page
    """
    xpath: str

    def __init__(self, title):
        """
        Initialize form field page text list item
        :param title: item title
        """
        self.xpath = format("//li[contains(text(), \"{}\")]]", str(title))


class FormFieldsElements:
    NAME_INPUT = (By.XPATH, "//input[@id=\"name-input\"]")
    PASSWORD_INPUT = (By.XPATH, "//input[@type=\"password\"]")

    DROPDOWN = (By.XPATH, "//select[@id=\"automation\"]")
    DROPDOWN_1 = ""
    DROPDOWN_2 = "Yes"
    DROPDOWN_3 = "No"
    DROPDOWN_4 = "Undecided"

    EMAIL_INPUT = (By.XPATH, "//input[@id=\"email\"]")
    MESSAGE_INPUT = (By.XPATH, "//textarea[@id=\"message\"]")

    """ List of checkboxes """
    CHECKBOXES = [
        FormFieldsCheckbox(1, "Water"),
        FormFieldsCheckbox(2, "Milk"),
        FormFieldsCheckbox(3, "Coffee"),
        FormFieldsCheckbox(4, "Wine"),
        FormFieldsCheckbox(5, "Ctrl-Alt-Delight"),
    ]

    """ List of radiobuttons """
    RADIOBUTTONS = [
        FormFieldsRadiobutton(1, "Red"),
        FormFieldsRadiobutton(2, "Blue"),
        FormFieldsRadiobutton(3, "Yellow"),
        FormFieldsRadiobutton(4, "Green"),
        FormFieldsRadiobutton(5, "#FFC0CB"),
    ]

    """ List of texts """
    TEXTLIST = [
        FormFieldsTextListItem("Selenium"),
        FormFieldsTextListItem("Playwright"),
        FormFieldsTextListItem("Cypress"),
        FormFieldsTextListItem("Appium"),
        FormFieldsTextListItem("Katalon Studio"),
    ]