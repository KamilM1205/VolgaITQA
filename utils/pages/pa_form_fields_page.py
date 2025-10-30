from selenium.webdriver.common.by import By, ByType
from selenium.webdriver.support.select import Select

from utils.locators.pa_form_fields import FormFieldsElements, FormFieldsCheckbox, FormFieldsRadiobutton
from utils.pages.base_page import BasePage


class PaFormFieldsPage(BasePage):
    """
    Methods for test page.
    """

    def enter_name(self, name: str) -> None:
        """
        Method for entering name in name field
        :param name: string that represents name
        :return: Nothing
        :raises: AssertionError if entered name is not equal to name
        """
        element = self.wait_element_visible(FormFieldsElements.NAME_INPUT)
        element.send_keys(name)

        if element.text != name:
            raise AssertionError("Entered name \"{}\" != \"{}\"".format(name, element.text))

    def enter_password(self, password: str) -> None:
        """
        Method for entering password in password field
        :param password: string that represents password
        :return: Nothing
        :raise: AssertionError if entered password is not equal to password
        """
        element = self.wait_element_visible(FormFieldsElements.PASSWORD_INPUT)
        element.send_keys(password)

        if element.text != password:
            raise AssertionError("Entered password \"{}\" != \"{}\"".format(element.text, password))

    def select_checkbox(self, checkbox: FormFieldsCheckbox) -> bool:
        """
        Selecting checkbox
        :param checkbox: checkbox that must be selected(or deselected)
        :return: checkbox state
        :raises: AssertionError if checkbox label is not equal to expected label
        """
        element = self.wait_element_clickable((By.XPATH, checkbox.checkbox_path))
        element.click()

        label = self.wait_element_visible((By.XPATH, checkbox.title_path))
        if label.text != checkbox.title:
            raise AssertionError("Checkbox label \"{}\" != \"{}\"".format(label, checkbox.title))

        return element.is_selected()

    def select_radiobutton(self, radiobutton: FormFieldsRadiobutton) -> bool:
        """
        Selecting radiobutton
        :param radiobutton: radiobutton that must be selected
        :return: checkbox state
        :raises: AssertionError if radiobutton label is not equal to expected label
        """
        element = self.wait_element_clickable((By.XPATH, radiobutton.radiobutton_path))
        element.click()

        label = self.wait_element_visible((By.XPATH, radiobutton.title_path))
        if label.text != radiobutton.title:
            raise AssertionError("Radiobutton label \"{}\" != \"{}\"".format(label, radiobutton.title))

        return element.is_selected()

    def select_dropdown(self, dropdown_value: str) -> None:
        """
        Selects dropdown item by them string value
        :param dropdown_value: item string value
        :return: Nothing
        :raises: AssertionError if dropdown selected item is not equal to dropdown_value
        """
        dropdown = Select(self.wait_element_clickable(FormFieldsElements.DROPDOWN))

        dropdown.select_by_value(dropdown_value)
        if self.get_dropdown_value() != dropdown_value:
            raise AssertionError("Dropdown selected value \"{}\" != \"{}\"".format(dropdown_value, dropdown_value))

    def get_dropdown_value(self) -> str:
        """
        Return current dropdown value
        :return: dropdown value
        """
        dropdown = Select(self.wait_element_visible(FormFieldsElements.DROPDOWN))
        return dropdown.first_selected_option.text

    def assert_text(self, text_path: tuple[ByType, str], expected_text: str) -> None:
        """
        Check element text equal with expected text
        :param text_path: XPath/Selector/etc to find element
        :param expected_text: text which we expect to find
        :return: Nothing
        :raise: AssertionError if element text is not equal to expected_text
        """
        element = self.wait_element_visible(text_path)

        if element.text != expected_text:
            raise AssertionError("Text \"{}\" != \"{}\"".format(element.text, expected_text))
