import pytest
from pages.login_page import LoginPage
from data import link, login_and_password, code, phone, defunct_login, get_password_for_login, incorrect_password
import time


@pytest.mark.parametrize('login', login_and_password)
def test_successful_authorization_login(browser, login):
    page = LoginPage(browser, link)
    page.open()
    page.jump_login_form()
    page.input_login_or_email(login)
    page.click_button_login()
    page.input_password(get_password_for_login(login))
    page.should_be_menu_profile()


def test_jump_authorization_phone(browser):
    page = LoginPage(browser, link)
    page.open()
    page.jump_phone_form()
    page.should_be_input_phone()


# Этот тест не пройдет, нужен функционал, который будет сохранять код для входа по телефону
def test_successful_authorization_phone(browser):
    page = LoginPage(browser, link)
    page.open()
    page.jump_phone_form()
    page.clear_field_phone()
    page.input_phone(phone)
    page.input_code_for_phone(code)
    page.should_be_menu_profile()


def test_authorization_defunct_login(browser):
    page = LoginPage(browser, link)
    page.open()
    page.jump_login_form()
    page.input_login_or_email(defunct_login)
    page.click_button_login()
    page.should_be_correct_error_defunct_login()


@pytest.mark.parametrize('login', login_and_password)
def test_unsuccessful_authorization_login(browser, login):
    page = LoginPage(browser, link)
    page.open()
    page.jump_login_form()
    page.input_login_or_email(login)
    page.click_button_login()
    page.input_password(incorrect_password)
    page.should_be_correct_error_unsuccessful_authorization_login()


def test_unsuccessful_authorization_phone(browser):
    page = LoginPage(browser, link)
    page.open()
    page.jump_phone_form()
    page.clear_field_phone()
    page.input_phone(phone)
    page.input_code_for_phone(code)
    page.should_be_correct_error_unsuccessful_authorization_phone()
