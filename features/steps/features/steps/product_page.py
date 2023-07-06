from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')
    sleep(2)


@then('Verify user can click colors')
def verify_can_click_colors(context):
    expected_colors = ['Light Wash', 'Black', 'Blue Over Dye', 'Rinsed']
    actual_colors = []

    colors = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")

    for color in colors[:4]:
        color.click()
        current_color = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name .selection").text
        actual_colors += [By.CSS_SELECTOR, "#variation_color_name .selection"]

    assert expected_colors == actual_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'