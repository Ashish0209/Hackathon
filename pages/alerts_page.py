from selenium.webdriver.common.by import By

class AlertsPage:
    def __init__(self, driver):
        # Store the driver instance passed from the test file and navigate to the JavaScript alerts demo page
        self.driver = driver
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    def handle_js_alert(self):
        # Click the button to trigger a simple JavaScript alert
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        alert = self.driver.switch_to.alert
        alert.accept()

    def handle_js_confirm(self):
        # Click the button to trigger a confirmation alert
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        alert = self.driver.switch_to.alert
        alert.accept()

    def handle_js_prompt(self, text):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def get_result(self):
        # Return the result message 
        return self.driver.find_element(By.ID, "result").text.strip()
