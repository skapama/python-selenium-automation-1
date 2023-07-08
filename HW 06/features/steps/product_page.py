from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
PRIVACY_NOTICE = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")
ORDERS_BTN = (By.ID, 'nav-orders')
POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button")
PRIVACY_NOTICE_BTN = (By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")

@given('Open amazon main page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com')

@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    context.driver.wait.until(
    EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
    message='Signin btn not clickable'
        ).click()

@then('Verify Sign In page opens')
def verify_signin_opens(context):
        # Verify URL:
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
        # Verify header
    actual_text = context.driver.find_element(*SIGNIN_HEADER).text
    expected_result = "Sign in"
    assert expected_result == actual_text, f'expected {expected_result}, but got {actual_text}'

@then('Click on Amazon Privacy & Condition Notice link')
def click_on_amazon_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE_BTN).click()

@then('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original:', context.original_window)
    print('All windows:', context.driver.window_handles)
@then('Click on Amazon Privacy Notice link')
def click_on_amazon_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()
@then('Switch to the newly opened window')
def switch_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    print('After window opened, all windows:', all_windows)
    context.driver.switch_to.window(all_windows[1])

@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/'))
@then('User can close new window and switch back to original')
def close_new_window(context):
    context.driver.switch_to.window(context.original_window)
    context.driver.close()