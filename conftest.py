import pytest
from selenium import webdriver
# import time


@pytest.fixture
def browser():
    print("\nstart browser")
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()
