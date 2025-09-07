from pages.base_page import BasePage
import random

class RegisterPage(BasePage):

    def get_title(self):
        return self.page.locator("h1.title").text_content().strip()

    def register_user(self, first="First name", last="Last name", password="Password"):
        username = str(random.randint(10000000, 99999999))
        address = "the 5th ring street"
        city = "Taiyuan"
        state = "Shanxi"
        zip_code = "041000"
        ssn = "1101142013"

        self.page.fill("#customer\\.firstName", first)
        self.page.fill("#customer\\.lastName", last)
        self.page.fill("#customer\\.username", username)
        self.page.fill("#customer\\.password", password)
        self.page.fill("#repeatedPassword", password)
        self.page.fill("#customer\\.address\\.street", address)
        self.page.fill("#customer\\.address\\.city", city)
        self.page.fill("#customer\\.address\\.state", state)
        self.page.fill("#customer\\.address\\.zipCode", zip_code)
        self.page.fill("#customer\\.ssn", ssn)

        self.page.click("input[value='Register']")

        return username, password

    def logout(self):
        from pages.home_page import HomePage
        
        self.page.click("a[href*='logout.htm']")
        return HomePage(self.page)
