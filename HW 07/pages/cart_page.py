from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


    CART_ICON = (By.ID, '#nav-cart-text-container')
    CART_EMPTY = (By.XPATH, '//*[@id="sc-active-cart"]/div/div/div[2]/div[1]/h2')

class CartPage(Page):
def open_main_page(self):
    self.open_url('https://www.amazon.com/')

def click_icon(self, context):
    self.verify_cart_icon(*self.CART_ICON)


def verify_cart_empty(self, context):
    self.verify_cart_empty(*self.CART_EMPTY)