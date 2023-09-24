from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.selenium_manager import SeleniumManager
import pytest


@pytest.fixture()
def setup(browser):

    global driver

    if browser == 'chrome':

        chrome_option = webdriver.ChromeOptions()
        chrome_option.set_capability("browserName", "chrome")
        chrome_option.add_argument('--incognito')
        SeleniumManager().driver_location(chrome_option)
        driver = webdriver.Chrome(options=chrome_option)
        driver.maximize_window()

    elif browser == 'firefox':
        firefox_option = Options()
        firefox_option.set_capability("browserName", "firefox")
        driver = webdriver.Firefox(options=firefox_option)

    else:
        chrome_option = webdriver.ChromeOptions()
        chrome_option.set_capability("browserName", "chrome")
        chrome_option.add_argument('--incognito')
        SeleniumManager().driver_location(chrome_option)
        driver = webdriver.Chrome(options=chrome_option)
        driver.maximize_window()

    yield driver
    driver.close()


def pytest_addoption(parser):  # this will get value from CLI hooks
    parser.addoption('--browsername')


@pytest.fixture()
def browser(request):   # this will return browser value to setup method
    return request.config.getoption('--browsername')



