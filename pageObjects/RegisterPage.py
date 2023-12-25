from selenium.webdriver.common.by import By


class Register:
    signup_linktext = "Create New account"
    textbox_name_id = "name"
    button_gender_class = "mat-radio-label"
    button_dob_icon_xpath = "//button[@class='mat-focus-indicator mat-icon-button mat-button-base']"
    button_dob_xpath = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator']"
    textbox_phone_id = "phone"
    textbox_email_id = "email"
    button_next_class = "btn"
    textbox_password_id = "password"
    textbox_confirmpassword_name = "confirmPassword"
    button_signup_xpath = "//button[@class='btn']"

    def __init__(self, driver):
        self.driver = driver

    def clicksignup(self):
        self.driver.find_element(By.LINK_TEXT, self.signup_linktext).click()

    def setname(self, name):
        self.driver.find_element(By.ID, self.textbox_name_id).clear()
        self.driver.find_element(By.ID, self.textbox_name_id).send_keys(name)

    def choosegender(self):
        self.driver.find_element(By.CLASS_NAME, self.button_gender_class).click()

    def clickdobicon(self):
        self.driver.find_element(By.XPATH, self.button_dob_icon_xpath).click()

    def choosedob(self):
        self.driver.find_element(By.XPATH, self.button_dob_xpath).click()

    def setphone(self, phone):
        self.driver.find_element(By.ID, self.textbox_phone_id).clear()
        self.driver.find_element(By.ID, self.textbox_phone_id).send_keys(phone)

    def setmail(self, mail):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(mail)

    def clicknext(self):
        self.driver.find_element(By.CLASS_NAME, self.button_next_class).click()

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def setconfirmpassword(self, cpassword):
        self.driver.find_element(By.NAME, self.textbox_confirmpassword_name).clear()
        self.driver.find_element(By.NAME, self.textbox_confirmpassword_name).send_keys(cpassword)

    def clicksign(self):
        self.driver.find_element(By.XPATH, self.button_signup_xpath).click()
