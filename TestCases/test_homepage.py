from ConfigData.config import TestData
from PageObjects.LoginPage import LoginPage


class Test_HomePage():


    def test_home_page_header(self, setup):

        self.driver = setup  # initialize  driver from conftest file
        lpobj = LoginPage(self.driver)  # LoginPage Object
        homeobj = lpobj.login(TestData.username, TestData.password)  # HomePage Object
        actual_header_value= homeobj.get_header_value()
        assert actual_header_value== TestData.homePageHeder # verify home page header

    def test_profile_img_visible(self,setup):
        self.driver = setup  # initialize  driver from conftest file
        lpobj = LoginPage(self.driver)  # LoginPage Object
        homeobj = lpobj.login(TestData.username, TestData.password) # HomePage Object
        homeobj.is_profile_img_visible()   # verify profile image






