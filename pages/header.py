from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN = (By.XPATH, "//*[@data-test='@web/AccountLink']")
    NAV_SIGNIN = (By.XPATH, "//*[@data-test='accountNav-signIn']")



    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart(self, cart):
        self.click(*self.CART_ICON)
        sleep(10)

    def click_sign_in(self):
        self.click(*self.SIGN_IN)
        sleep(10)

    def click_nav_signin(self):
        self.click(*self.NAV_SIGNIN)
        sleep(10)
