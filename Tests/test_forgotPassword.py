from pageObjects.ForgotPassword import ForgotPassword
import allure
from allure_commons.types import AttachmentType
from utilities.readProperties import *
import time

readConfig = ReadConfig()


class TestForgotpassword:
    baseURL = readConfig.get_url()
    email = readConfig.get_username()

    def test_forgotpassword(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.fp = ForgotPassword(self.driver)
        self.fp.clickforgotpassword()
        time.sleep(2)
        self.fp.setemail(self.email)
        self.fp.clicksend()

        allure.attach(self.driver.get_screenshot_as_png(), name="TestForgotpassword", attachment_type=AttachmentType.PNG)
        self.driver.close()
