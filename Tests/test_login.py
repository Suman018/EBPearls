from pageObjects.LoginPage import Login


class TestLogin:
    baseUrl = "https://parabank.parasoft.com/parabank/index.htm"
    username = "suman"
    password = "suman786"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.driver.close()
