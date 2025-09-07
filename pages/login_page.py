from pages.base_page import BasePage
from pages.account_page import AccountPage

class LoginPage(BasePage):
    def login(self, username, password):
        self.page.fill("input[name='username']", username)
        self.page.fill("input[name='password']", password)
        self.page.click("input[value='Log In']")
        self.page.wait_for_selector("h1.title")

        return AccountPage(self.page)
