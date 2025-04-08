import pytest
from pages.login_page import LoginPage
from utils.driver_setup import get_lambda_driver
from utils.env import USERNAME, PASSWORD

@pytest.mark.parametrize("username,password,expected", [
    (USERNAME, PASSWORD, "You logged into a secure area!"),
    ("wronguser", "wrongpass", "Your username is invalid!")
])
def test_login(username, password, expected):
    driver = get_lambda_driver("Login Test")
    login = LoginPage(driver)
    login.login(username, password)
    assert expected in login.get_message()
    driver.quit()