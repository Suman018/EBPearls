from selenium.webdriver.common.by import By


class ForgotPassword:
    textbox_username_id = "email"
    button_send_class = "btn"
    forgot_password_class = "forgot-password"

    def __init__(self, driver):
        self.driver = driver

    def clickforgotpassword(self):
        self.driver.find_element(By.CLASS_NAME, self.forgot_password_class).click()

    def setemail(self, email):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(email)

    def clicksend(self):
        self.driver.find_element(By.CLASS_NAME, self.button_send_class).click()
