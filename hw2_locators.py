from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# By ID
driver.find_element(By.ID, 'auth-fpp-link-bottom')
driver.find_element(By.ID, 'nav-search-submit-button')

# By Xpath, Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
# By Xpath, Continue button
driver.find_element(By.XPATH, "//input[@class='a-button-input']")

#By Xpath, Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# By ID, Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# By ID, Other issues with Sign-in link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# By ID, create your amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

# By Xpath, condition of use link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")

# By Xpath, Privacy Notice
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_privacy_notice')]")

