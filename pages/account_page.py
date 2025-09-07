from pages.base_page import BasePage

class AccountPage(BasePage):

    def get_heading(self):
        return self.page.get_by_role("heading", name="Accounts Overview").text_content().strip()

    def go_to_open_new_account(self):
        self.page.click("a[href='openaccount.htm']")
        self.page.wait_for_selector("#type") # wait for the dropdown list


    def open_new_account(self, account_type="SAVINGS"):
        self.page.select_option("#type", account_type)
        self.page.wait_for_timeout(500)
        self.page.click("input[value='Open New Account']")

        locator = self.page.locator("#newAccountId")

        self.page.wait_for_function(
            """() => {
                const el = document.querySelector('#newAccountId');
                return el && el.textContent.trim().length > 0;
            }"""
        )

        return locator.text_content().strip()

    
    def go_to_accounts_overview(self):
        self.page.click("a[href='overview.htm']")
        self.page.wait_for_selector("h1.title")

    def get_account_balance(self, account_id):
        row_locator = self.page.locator(f"tr:has-text('{account_id}')")
        row_locator.wait_for()
        
        # balance column is the 2nd column
        balance_text = row_locator.locator("td").nth(1).text_content()
        return float(balance_text.replace("$", "").replace(",", "").strip())
