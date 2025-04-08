import pytest
from pages.alerts_page import AlertsPage
from utils.driver_setup import get_lambda_driver

def test_js_alert():
    driver = get_lambda_driver("JS Alert Test")
    alerts = AlertsPage(driver) #Create an instance of AlertsPage
    alerts.handle_js_alert()
    # Validate the result message
    assert "You successfully clicked an alert" in alerts.get_result()
    driver.quit()

def test_js_confirm():
    driver = get_lambda_driver("JS Confirm Test")
    alerts = AlertsPage(driver)
    alerts.handle_js_confirm() #Trigger and accept the JS Confirm dialog
    assert "You clicked: Ok" in alerts.get_result()
    driver.quit()

def test_js_prompt():
    driver = get_lambda_driver("JS Prompt Test")
    alerts = AlertsPage(driver)
    alerts.handle_js_prompt("Ashish")
    #Assert the entered text
    assert "You entered: Ashish" in alerts.get_result()
    driver.quit()
