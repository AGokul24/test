from seleniumbase import BaseCase

class loginTest(BaseCase):
    def test_loginPage(self):
        # open webpage

        self.open("http://admin-demo.nopcommerce.com")
        self.maximize_window()
        # assert title
        self.assert_title("Your store. Login")
        # assert loginpage
        self.assert_element("//strong[text()]")
        # username & password
        self.clear("//input[@name='Email']")
        self.type("//input[@name='Email']", "admin@yourstore.com")
        self.clear("//input[@class='password']")
        self.type("//input[@class='password']", "admin")
        # click login
        self.click("//button[@type='submit']")
        #assert verify

    def test_homePage(self):
        pass
