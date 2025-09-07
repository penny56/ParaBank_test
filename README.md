I have 7 years of work experience with Python in test automation. Could I finish this quiz with Python, and if TypeScript and JavaScript are mandatory in the future, if I get the chance, I can learn them in very short time.

Here are some details about two test scenarios:

- **UI Test scenarios**:  
  Use `BasePage` as the parent class. Each page is a child class. When I need to work with a different page, I create an object of that page class and call its member functions.  
  For example:  
  - `RegisterPage` class has `register_user()` method.  
  - `AccountPage` class has `open_new_account()` and `get_account_balance()` methods.  

  When running `login()`, cookie data is saved into a `cookie.json` file in the project root. This file is used later for API tests.  
  In Step 8, the bill pay data is written into a JSON file and stored in the project root. This file is also used in API test cases for validation.  

- **API Test scenarios**:  
  By checking the **Network** tab in browser *Inspect*, I found the `find transactions` base URL and the `amount` parameter.  
  With the cookie file saved before, I can send an HTTP request and get the response.  
  Then I compare the response with the JSON file created in the UI test, to make sure the data found by `find transactions` matches the stored data.  

- **Auto Test**:  
  This project is integrated with GitHub Actions to perform auto testing. Once a commit is submitted to the main branch, GitHub Actions will automatically start to run the test cases.

