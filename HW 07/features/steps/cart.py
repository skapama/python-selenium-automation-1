from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

CART_ICON = (By.ID, '#nav-cart-text-container')
CART_EMPTY = (By.XPATH, '//*[@id="sc-active-cart"]/div/div/div[2]/div[1]/h2')

@given('Open amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.cart_page.open_main_page()

@when('Click on cart icon')
def click_cart(context):
    context.app.cart_page.click_icon()

@then('Verify Shopping Cart is empty')
def verify_cart_empty(context):
    actual_text = context.driver.find_element(*CART_EMPTY).text
