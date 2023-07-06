from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


ORDERS_BTN = (By.ID, 'nav-orders')
SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a')
POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button")


@given('Open amazon main page')
@@ -29,6 +32,14 @@ def click_orders(context):
    context.driver.find_element(*ORDERS_BTN)


@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin btn not clickable'
    ).click()


@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    expected_amount = int(expected_amount)