from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then('Verify search results shown for {expected_result}')
def verify_cart_is_empty(context):
    actual_result = context.driver.find_element(By.XPATH, "//a[@href='/gp/goldbox/ref=cart_empty_deals']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'