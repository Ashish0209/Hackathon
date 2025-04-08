from selenium.webdriver.common.by import By

class AlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    def handle_js_alert(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        alert = self.driver.switch_to.alert
        alert.accept()

    def handle_js_confirm(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        alert = self.driver.switch_to.alert
        alert.accept()

    def handle_js_prompt(self, text):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def get_result(self):
        return self.driver.find_element(By.ID, "result").text.strip()