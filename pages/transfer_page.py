from pages.base_page import BasePage

class TransferPage(BasePage):
    def go_to_transfer_page(self):
        self.page.click("a[href='transfer.htm']")
        self.page.wait_for_selector("#fromAccountId")

    def transfer_funds(self, from_acc, to_acc, amount):
        self.page.select_option("#fromAccountId", from_acc)
        self.page.select_option("#toAccountId", to_acc)
        self.page.fill("#amount", str(amount))
        self.page.click("input[value='Transfer']")

        result_locator = self.page.locator("h1.title").filter(has_text="Transfer Complete!")
        result_locator.wait_for(timeout=10000)

        result_text = result_locator.text_content()
        return result_text.strip()