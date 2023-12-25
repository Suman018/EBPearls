import pytest
from allure_commons.types import AttachmentType

from pageObjects.Loginpage import *
import allure



class TestForgotpassword:
    baseURL = "https://qa-cms-rcwl.remotecoach.fit/"
    forgot_password= '//*[@id="kt_sign_in_form"]/div[4]/a'
    forgotpassword_textbox = 'bishnu+admin@remotecoach.fit'


    def test_forgotpassword(self,setup):
        self.driver = setup
        self.loginPageDriver = LoginPage(self.driver)
        self.loginPageDriver.open_page(self.baseURL)
        self.loginPageDriver.click_forgotpassword(self.forgot_password)
        self.loginPageDriver.enter_forgotpassword_textbox(self.forgotpassword_textbox)
        self.loginPageDriver.click_submit_button()
        allure.attach(self.driver.get_screenshot_as_png(),name="TestForgotpassword",attachment_type=AttachmentType.PNG)
        self.driver.close()