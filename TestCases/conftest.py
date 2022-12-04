from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
import pytest


@pytest.fixture()
def setup(browser):

    global driver

    if browser == 'chrome':
        SeleniumManager.driver_location('chrome')
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument('--incognito')
        driver = webdriver.Chrome(options=chrome_option)

    if browser == 'firefox':
        SeleniumManager.driver_location('firefox')
        driver = webdriver.Firefox()

    else:
        SeleniumManager.driver_location('chrome')
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument('--incognito')
        driver = webdriver.Chrome(options=chrome_option)

    yield driver
    driver.close()


def pytest_addoption(parser):  # this will get value from CLI hooks
    parser.addoption('--browsername')


@pytest.fixture()
def browser(request):   # this will return browser value to setup method
    return request.config.getoption('--browsername')



