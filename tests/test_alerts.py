import pytest
from pages.alerts_page import AlertsPage
from utils.driver_setup import get_lambda_driver

def test_js_alert():
    driver = get_lambda_driver("JS Alert Test")
    alerts = AlertsPage(driver)
    alerts.handle_js_alert()
    assert "You successfully clicked an alert" in alerts.get_result()
    driver.quit()

def test_js_confirm():
    driver = get_lambda_driver("JS Confirm Test")
    alerts = AlertsPage(driver)
    alerts.handle_js_confirm()
    assert "You clicked: Ok" in alerts.get_result()
    driver.quit()

def test_js_prompt():
    driver = get_lambda_driver("JS Prompt Test")
    alerts = AlertsPage(driver)
    alerts.handle_js_prompt("Ashish")
    assert "You entered: Ashish" in alerts.get_result()
    driver.quit()