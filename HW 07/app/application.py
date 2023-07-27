
from pages.cart_page import CartPage
from pages.signin_page import SignInPage


class Application:

    def __init__(self, driver):
        self.driver = driver


        self.cart_page = CartPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)