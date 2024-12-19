from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SigninPage(BasePage):


    def verify_cart_empty(self):
        #self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)