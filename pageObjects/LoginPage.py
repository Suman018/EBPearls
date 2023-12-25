
class Login:
    textbox_username_id = "username"
    textbox_password_name = "password"
    button_login_xpath = "//input[@class='button']"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_name(self.textbox_username_id).clear()
        self.driver.find_element_by_name(self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_name(self.textbox_password_name).clear()
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
