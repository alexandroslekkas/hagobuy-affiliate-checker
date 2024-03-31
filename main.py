import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('https://www.hagobuy.com/login')
browser.implicitly_wait(5)

username_field = browser.find_element(By.NAME, 'username')
password_field = browser.find_element(By.NAME, 'password')

username_field.send_keys(account_email = os.environ['ACCOUNT_EMAIL'])
password_field.send_keys(account_email = os.environ['ACCOUNT_PASSWORD'])

login_button = browser.find_element(By.XPATH, "//div[contains(text(),'Login')]")
login_button.click()

browser.implicitly_wait(5)

if browser.current_url == 'https://www.hagobuy.com/':
    print("Successfully logged in!")
else:
    print("Login failed or the expected URL does not match.")