from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
BEST_SELLER_LINKS = (By.CSS_SELECTOR, 'div#zg_header a')


@given('Open amazon best seller page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@when('Search for {search_query}')
def search_amazon(context, search_query):
    context.driver.find_element(*SEARCH_FILED).send_keys(search_query)
    context.driver.find_element(*SEARCH_BTN).click()

@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    print('After conversion: => ', type(expected_amount))

    links_count = len(context.driver.find_elements(*BEST_SELLER_LINKS)) # 5
    print(type(links_count))

    # 5 == 5
    assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'


