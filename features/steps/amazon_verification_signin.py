from selenium.webdriver.common.by import By
from behave import given, when, then



@then('Verify search results shown for {expected_result}')
def verify_signin_opens(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == 'Sign in', f'Error! Expected Sign in header bot got actual {actual_result}'
    context.driver.find_element(by.ID, 'ap_email')