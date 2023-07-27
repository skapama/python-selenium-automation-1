from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

ORDERS_BTN = (By.ID, 'nav-orders')
SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
RESULT_TEXT =  (By.XPATH, '//*[@id="sc-active-cart"]/div/div/div[2]/div[1]/h2')


class SignInPage(Page):
def open_main_page(self):
    self.open_url('https://www.amazon.com/')

def search_amazon(self, search_query):
     self.input_text(search_query, *self.SEARCH_FILED)
     self.click(*self.SEARCH_BTN)

def click_orders(self, context):
    self.click_order(*self.SEARCH_BTN)

def verify_search_results(self, expected_result):
    self.verify_search_text(expected_result, *self.RESULT_TEXT)
