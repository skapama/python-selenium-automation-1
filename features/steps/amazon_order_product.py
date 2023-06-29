from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


