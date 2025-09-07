import pytest
from playwright.sync_api import sync_playwright
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.account_page import AccountPage
from pages.transfer_page import TransferPage
from pages.billpay_page import BillPayPage
import time
import json

BASE_URL = "https://parabank.parasoft.com/"

def test_ui_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        context = browser.new_context()
        page = context.new_page()

        # step 1, open Para bank home page
        home_page = HomePage(page)
        home_page.goto(BASE_URL)
        assert "ParaBank" in home_page.get_title()


        # step 2, create a new user
        register_page = home_page.go_to_register()
        assert register_page.get_title() == "Signing up is easy!"

        username, password = register_page.register_user()
        assert register_page.get_title() == "Welcome " + username
        register_page.page.wait_for_timeout(1000)
        home_page = register_page.logout()


        # step 3, login
        login_page = LoginPage(page)
        account_page = login_page.login(username, password)
        assert account_page.get_heading() == "Accounts Overview"

        # save the cookie info to json file for api test usage
        with open("cookie.json", "w") as f:
            json.dump(context.cookies()[0], f)  

        # record the existing old_account_id
        old_account_id = page.locator("table#accountTable tbody tr td a").first.inner_text().strip()

        login_page.page.wait_for_timeout(1000)

        # step 4, very global navigation manual
        home_page.go_to_about_us()
        assert "About Us" in page.title()

        home_page.go_to_services()
        assert "Services" in page.title()

        home_page.go_to_products()
        home_page.back_to_home()

        home_page.go_to_locations()
        home_page.back_to_home()

        home_page.go_to_admin_page()
        assert "Administration" in page.title()
        home_page.back_to_home()

        
        # step 5, Open New Account Page, capture the account number
        account_page = AccountPage(page)
        account_page.go_to_open_new_account()
        new_account_id = account_page.open_new_account("SAVINGS")

        assert new_account_id is not None

        # step 6, Validate if Accounts overview page is displaying the balance details as expected.
        account_page.go_to_accounts_overview()
        new_account_balance = account_page.get_account_balance(new_account_id)

        # step 7, Transfer funds from account to another account.
        # Confirm the transfer amount is less than balance
        # assert new_account_balance >= 1, "Transfer amount exceeds available balance"

        transfer_page = TransferPage(page)
        transfer_page.go_to_transfer_page()
        confirmation = transfer_page.transfer_funds (from_acc=new_account_id, to_acc=old_account_id, amount=1.0)
        assert "Transfer Complete" in confirmation


        # step 8, Pay the bill
        bill_pay_page = BillPayPage(page)
        bill_pay_page.go_to_bill_pay_page()
        result = bill_pay_page.pay_bill(new_account_id, 1)
        assert result == "Bill Payment Complete"

        print("UI Test scenarios: completed!")

