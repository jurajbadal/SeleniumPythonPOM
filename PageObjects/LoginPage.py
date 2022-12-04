from selenium.webdriver.common.by import By

from ConfigData.config import TestData
from PageObjects.BasePage import BasePage
from PageObjects.HomePage import HomePage


class LoginPage(BasePage):
    txt_USERNAME = (By.XPATH, '//input[@name="username"]')
    txt_PASSWORD = (By.XPATH, '//input[@name="password"]')
    btn_LOGIN = (By.XPATH, '//button[@type="submit"]')
    lnk_FORGOT_PASSWORD = (By.CSS_SELECTOR, '[class*=login-forgot]>p')

    def __init__(self, driver):
        super().__init__(driver)

    def verify_title(self, title):
        return self.get_title(title)

    def login(self, username, password):
        self.do_send_keys(self.txt_USERNAME, username)  # set username
        self.do_send_keys(self.txt_PASSWORD, password)  # set password
        self.do_click(self.btn_LOGIN)
        return HomePage(self.driver)

    def is_forgot_password_link_is_visible(self):
        return self.element_is_visible(self.lnk_FORGOT_PASSWORD)
