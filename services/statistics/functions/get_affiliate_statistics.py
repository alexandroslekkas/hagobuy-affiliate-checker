from utilities.strings import get_clean_number

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Function to get the current affiliate statistics
def get_affiliate_statistics():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enables headless mode
    chrome_options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options)
    browser.get('https://www.hagobuy.com/login')

    username_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    username_field.send_keys(os.environ['HAGOBUY_ACCOUNT_EMAIL'])
    password_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    password_field.send_keys(os.environ['HAGOBUY_ACCOUNT_PASSWORD'])

    login_button_container = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ant-spin-container'))
    )
    login_button = login_button_container.find_element(By.XPATH, ".//div[contains(text(), 'Login')]")
    login_button.click()

    time.sleep(2.5)
    
    browser.get('https://www.hagobuy.com/center/affiliates')

    time.sleep(4.5)

    wait = WebDriverWait(browser, 10)

    available_bonus_balance = get_clean_number(wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(text(), 'Available bonus balance')]/following-sibling::div")
    )).text)
    unsettled_amount = get_clean_number(wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(text(), 'Unsettled amount')]/following-sibling::div")
    )).text)
    bonus_earned = get_clean_number(wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(text(), 'Bonus earned')]/following-sibling::div")
    )).text)
    number_of_invited = get_clean_number(wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(text(), 'Number of invited')]/following-sibling::div")
    )).text)
    recommended_order = get_clean_number(wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(text(), 'Recommended order')]/following-sibling::div")
    )).text)

    return available_bonus_balance, unsettled_amount, bonus_earned, number_of_invited, recommended_order