import pytest
from pages.login_page import LoginPage
from utils.driver_setup import get_lambda_driver
from utils.env import USERNAME, PASSWORD

@pytest.mark.parametrize("username,password,expected", [
    (USERNAME, PASSWORD, "You logged into a secure area!"),  # Valid credentials
    ("wronguser", "wrongpass", "Your username is invalid!")  # Invalid credentials
])
def test_login(username, password, expected):
    # Initialize
    driver = get_lambda_driver("Login Test")
    login = LoginPage(driver)  #instance of the LoginPage and navigate to the login page
    login.login(username, password)
    assert expected in login.get_message()
    driver.quit()
