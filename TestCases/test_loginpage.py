from ConfigData.config import TestData
from PageObjects.LoginPage import LoginPage

class Test_Login():

    def test_login(self,setup):

        self.driver = setup  # initialize  driver from conftest file
        lpobj = LoginPage(self.driver)  # LoginPage Object
        lpobj.verify_title(TestData.loginPageTitle)
        is_link_visible = lpobj.is_forgot_password_link_is_visible()
        assert is_link_visible == True
        lpobj.login(TestData.username, TestData.password)  # login