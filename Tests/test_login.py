from pageObjects.LoginPage import Login
import allure
from allure_commons.types import AttachmentType
from utilities.readProperties import *

readConfig = ReadConfig()


class TestLogin:
    baseUrl = readConfig.get_url()
    username = readConfig.get_username()
    password = readConfig.get_password()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        allure.attach(self.driver.get_screenshot_as_png(), name="test_login_page", attachment_type=AttachmentType.PNG)
        self.driver.close()
