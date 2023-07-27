from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL = (By.ID, 'ap_email')


@given('Open amazon main page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.signin_page.open_main_page()

@when('Search for {search_query}')
def search_amazon(context, search_query):
    context.app.signin_page.search_amazon(search_query)


@when('Click Amazon Orders link')
def click_orders(context):
    context.app.signin_page.click_orders()


@then('Verify Sign In page opens')
def verify_signin_opens(context):
    # Verify URL:
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
    # Verify header
    actual_text = context.driver.find_element(*SIGNIN_HEADER).text
    assert actual_text == 'Sign in', f'Expected Sign in header but got {actual_text}'
    # Verify email field present
    context.driver.find_element(*EMAIL)