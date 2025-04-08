from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        # Store the driver instance passed from the test file
        self.driver = driver
        # Navigate to the login page
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        # Find the username and password input field and enter the provided username
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        # Click the login button to submit the form
        self.driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    def get_message(self):
         # Return the flash message text (success or error message shown after login attempt)
        return self.driver.find_element(By.ID, "flash").text.strip()
