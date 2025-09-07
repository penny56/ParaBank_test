from pages.base_page import BasePage
import json

class BillPayPage(BasePage):
    
    def go_to_bill_pay_page(self):
        self.page.click("a[href='billpay.htm']")
        self.page.wait_for_selector("h1.title:text('Bill Payment Service')")
        

    def pay_bill(self, from_acc, amount):
        self.page.wait_for_selector("#billpayForm select[name='fromAccountId']", state="visible")
        self.page.select_option("#billpayForm select[name='fromAccountId']", from_acc)

        self.page.fill("#billpayForm input[name='payee.name']", "Jim")
        self.page.fill("#billpayForm input[name='payee.address.street']", "6th ring street")
        self.page.fill("#billpayForm input[name='payee.address.city']", "Beijing")
        self.page.fill("#billpayForm input[name='payee.address.state']", "Shanxi")
        self.page.fill("#billpayForm input[name='payee.address.zipCode']", "041000")
        self.page.fill("#billpayForm input[name='payee.phoneNumber']", "18611112222")
        self.page.fill("#billpayForm input[name='payee.accountNumber']", "12345")
        self.page.fill("#billpayForm input[name='verifyAccount']", "12345")
        
        self.page.fill("#billpayForm input[name='amount']", str(amount))

        self.page.click("input[value='Send Payment']")

        result_locator = self.page.locator("h1.title").filter(has_text="Bill Payment Complete")
        result_locator.wait_for(timeout=10000, state="visible")

        # fill in the json file
        step8_payment_data = {
            "account_id": from_acc,
            "amount": amount,
            "payee_name": "Jim"
        }

        with open("step8_payment_data.json", "w") as f:
            json.dump(step8_payment_data, f)        

        result_text = result_locator.text_content()
        return result_text.strip()
