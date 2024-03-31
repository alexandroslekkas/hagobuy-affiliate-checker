import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print("[>] Navigating to https://www.hagobuy.com/login")
browser.get('https://www.hagobuy.com/login')

print("[!] On login page, waiting for fields...")
username_field = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'username'))
)
password_field = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'password'))
)

print("[>] Sending email and password")
username_field.send_keys(os.environ['ACCOUNT_EMAIL'])
password_field.send_keys(os.environ['ACCOUNT_PASSWORD'])

print("[>] Clicking on the login button")
login_button_container = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'ant-spin-container'))
)
login_button = login_button_container.find_element(By.XPATH, ".//div[contains(text(), 'Login')]")
login_button.click()

time.sleep(3)

print("[>] Navigating to the affiliate center...")
browser.get('https://www.hagobuy.com/center/affiliates')

# Install the python-telegram-bot package using pip
# pip install python-telegram-bot

import asyncio
from telegram import Bot

async def send_async_message(message):
    bot_token = os.environ['BOT_TOKEN']
    bot_chatID = '6675952317'

    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=bot_chatID, text=message)

asyncio.run(send_async_message("Testing connection!"))
                                        