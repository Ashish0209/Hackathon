from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.env import LT_USERNAME, LT_ACCESS_KEY
import os

def get_lambda_driver(test_name):
    options = Options()

    lt_options = {
        "username": LT_USERNAME,
        "accessKey": LT_ACCESS_KEY,
        "platformName": "Windows 10",
        "project": "QA Hackathon",
        "build": "Hackathon Tests",  # build name to group tests together
        "name": test_name,
        "selenium_version": "4.0.0"
    }

    options.set_capability('browserName', 'Chrome')
    options.set_capability('browserVersion', 'latest')
    options.set_capability('LT:Options', lt_options)

    url = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub"
    return webdriver.Remote(command_executor=url, options=options)

print(f"LT_USERNAME: {LT_USERNAME}")
print(f"LT_ACCESS_KEY: {LT_ACCESS_KEY}")
