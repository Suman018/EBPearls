from pageObjects.RegisterPage import Register
import time
from utilities.readProperties import *
from faker import Faker
faker = Faker()

readConfig = ReadConfig()


class TestRegister:
    baseUrl = readConfig.get_url()
    fake_email = faker.email()
    fake_name = faker.name()
    phone = "98" + str(faker.random_number(digits=8))
    password = "Test@123"
    confirm_password = "Test@123"

    def test_register(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.ru = Register(self.driver)
        self.ru.clicksignup()
        time.sleep(2)
        self.ru.setname(self.fake_name)
        self.ru.choosegender()
        self.ru.clickdobicon()
        self.ru.choosedob()
        self.ru.setphone(self.phone)
        self.ru.setmail(self.fake_email)
        self.ru.clicknext()
        time.sleep(2)
        self.ru.setpassword(self.password)
        self.ru.setconfirmpassword(self.confirm_password)
        time.sleep(2)
        self.ru.clicksign()

        self.driver.close()
