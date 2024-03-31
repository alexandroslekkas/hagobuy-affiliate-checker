import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Function to get the current affiliate statistics
def get_affiliate_statistics():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get('https://www.hagobuy.com/login')

    username_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    username_field.send_keys(os.environ['ACCOUNT_EMAIL'])
    password_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    password_field.send_keys(os.environ['ACCOUNT_PASSWORD'])

    login_button_container = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ant-spin-container'))
    )
    login_button = login_button_container.find_element(By.XPATH, ".//div[contains(text(), 'Login')]")
    login_button.click()

    time.sleep(2.5)
    
    browser.get('https://www.hagobuy.com/center/affiliates')