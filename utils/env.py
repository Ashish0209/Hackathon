from dotenv import load_dotenv
import os

load_dotenv()

LT_USERNAME = os.getenv("LT_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")
USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")

print(f"Loaded USERNAME: {USERNAME}")
print(f"Loaded PASSWORD: {PASSWORD}")