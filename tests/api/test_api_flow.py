import pytest
import requests
import json
from pathlib import Path


BASE_URL = "https://parabank.parasoft.com/parabank/services/bank"

def find_transactions(account_id, amount, cookie_data):

    session_id = cookie_data["value"]
    cookies = {"JSESSIONID": session_id}
    headers = {'Accept': 'application/json'}
    url = f"{BASE_URL}/accounts/{account_id}/transactions/amount/{amount}"
    response = requests.get(url, verify=False, timeout=30, cookies=cookies, headers=headers)  # turn off SSL
    response.raise_for_status()

    return json.loads(response.text)


@pytest.fixture
def step8_payment_data():
    project_root = Path(__file__).resolve().parent.parent.parent
    json_path = project_root / "step8_payment_data.json"
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture
def cookie_data():
    project_root = Path(__file__).resolve().parent.parent.parent
    json_path = project_root / "cookie.json"
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_find_transaction_by_amount(step8_payment_data, cookie_data):
    account_id = step8_payment_data["account_id"]
    amount = step8_payment_data["amount"]

    transactions = find_transactions(account_id, amount, cookie_data)
    assert transactions is not None, "API did not return JSON response"

    assert len(transactions) > 0, "No transactions found for the given amount"

    matched = False
    for transaction in transactions:
        if transaction["amount"] == amount and str(transaction["accountId"]) == account_id:
            matched = True
    assert matched, "No matching transaction found"

    print("API Test scenarios: completed!")