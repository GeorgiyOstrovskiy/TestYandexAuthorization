from .base_page import BasePage
from locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys
from data import error_authorization_defunct_login, error_unsuccessful_authorization_login, \
    error_unsuccessful_authorization_phone, login_and_password


class LoginPage(BasePage):
    def input_login_or_email(self, value):
        self.browser.find_element(*LoginPageLocators.FIELD_LOGIN).send_keys(value)

    def click_button_login(self):
        self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN).click()

    def input_password(self, value):
        self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD_FOR_LOGIN).send_keys(value, Keys.ENTER)

    def should_be_menu_profile(self):
        assert self.is_element_present(*LoginPageLocators.MENU_BUTTON), 'Error authorization'

    def jump_phone_form(self):
        self.browser.find_element(*LoginPageLocators.PHONE_FORM).click()

    def jump_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM).click()

    def clear_field_phone(self):
        self.browser.find_element(*LoginPageLocators.FIELD_PHONE).clear()

    def input_phone(self, value):
        self.browser.find_element(*LoginPageLocators.FIELD_PHONE).send_keys(value, Keys.ENTER)

    def input_code_for_phone(self, value):
        self.browser.find_element(*LoginPageLocators.FIELD_CODE_FOR_PHONE).send_keys(value, Keys.ENTER)

    def should_be_input_phone(self):
        assert self.is_element_present(*LoginPageLocators.FIELD_PHONE), 'Login form on phone is not presented'

    def should_be_correct_error_defunct_login(self):
        error = self.browser.find_element(*LoginPageLocators.ERROR_DEFUNCT_LOGIN).text
        assert error == error_authorization_defunct_login, 'Incorrect error'

    def should_be_correct_error_unsuccessful_authorization_login(self):
        error = self.browser.find_element(*LoginPageLocators.ERROR_UNSUCCESSFUL_AUTHORIZATION).text
        assert error == error_unsuccessful_authorization_login, 'Incorrect error'

    def should_be_correct_error_unsuccessful_authorization_phone(self):
        error = self.browser.find_element(*LoginPageLocators.ERROR_UNSUCCESSFUL_AUTHORIZATION_PHONE).text
        print(error)
        assert error == error_unsuccessful_authorization_phone, 'Incorrect error'
