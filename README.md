🚀 QA Hackathon - Login & JavaScript Alerts Automation

This project is part of a QA Hackathon challenge to automate a login flow and JavaScript alert handling using Selenium and LambdaTest.

------------------------------------------------------------
💡 Project Overview

The goal was to automate:
- A secure login process
- Handling JavaScript alerts like Alert, Confirm, and Prompt

The tests run on the cloud using LambdaTest and generate HTML reports.

------------------------------------------------------------
🛠️ Tech Stack

- Python
- Selenium
- Pytest
- LambdaTest for cross-browser testing
- dotenv for loading sensitive info
- pytest-html for reports
- pytest-xdist for parallel test execution
- pytest-rerunfailures to rerun flaky tests

------------------------------------------------------------
🔐 Secure Credentials

Credentials (like login username, password, LambdaTest keys) are stored in a `.env` file and never hardcoded in the code.

Example .env file:
APP_USERNAME=your_username
APP_PASSWORD=your_password
LT_USERNAME=your_lambdatest_username
LT_ACCESS_KEY=your_lambdatest_access_key

------------------------------------------------------------
🧪 How to Run the Tests

1. Activate your virtual environment

    python -m venv venv

2. On Windows:

    venv\Scripts\activate

3.  Install dependencies (including pytest)

    pip install -r requirements.txt

4. Run the Test

    pytest -n 2 --html=report.html 
           OR
    pytest -n 2 tests/ --html=report.html --reruns 1

------------------------------------------------------------
📋 My Thought Process

- I kept the code modular by separating driver setup, environment handling, and tests.
- Ensured no sensitive data is exposed in code.
- Made it parallel-friendly to save test time.
- Integrated LambdaTest for real browser coverage.
- Generated a clean HTML report so test results are easy to view and share.

------------------------------------------------------------
📂 Project Structure

login_and_Alert_automation/
│
├── tests/
│   ├── test_login.py
│   └── test_alerts.py
│
├── utils/
│   ├── driver_setup.py
│   └── env.py
│
├── .env
├── requirements.txt
└── report.html

------------------------------------------------------------
🌐 LambdaTest

All tests run on LambdaTest infrastructure.
Here is the Build Link to check all the tests run on the LamdaTest -->
https://automation.lambdatest.com/share?shareId=H89W94X0OKXFI6OO8JF7X1F8JP12QXPIGAYHN9NXE7WJAMOUBIUPSZYK3LBJ0UCP&isThemeEnabled=true&themeVersion=v2

------------------------------------------------------------
📸 Report

After running tests, view the generated `report.html` in your browser.

------------------------------------------------------------
