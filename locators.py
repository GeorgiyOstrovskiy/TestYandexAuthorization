from selenium.webdriver.common.by import By


class LoginPageLocators:
    FIELD_LOGIN = (By.ID, 'passp-field-login')
    BUTTON_LOGIN = (By.ID, r'passp:sign-in')
    FIELD_PASSWORD_FOR_LOGIN = (By.ID, 'passp-field-passwd')
    MENU_BUTTON = (By.CSS_SELECTOR, '[aria-label="Меню профиля"] button')
    PHONE_FORM = (By.CSS_SELECTOR, '[data-type="phone"]')
    LOGIN_FORM = (By.CSS_SELECTOR, '[data-type="login"]')
    FIELD_PHONE = (By.CLASS_NAME, 'Textinput-Control_phone')
    FIELD_CODE_FOR_PHONE = (By.ID, 'passp-field-phoneCode')
    ERROR_DEFUNCT_LOGIN = (By.ID, r'field:input-login:hint')
    ERROR_UNSUCCESSFUL_AUTHORIZATION = (By.ID, r'field:input-passwd:hint')
    ERROR_UNSUCCESSFUL_AUTHORIZATION_PHONE = (By.ID, r'field:input-phoneCode:hint')
