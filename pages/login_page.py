from symtable import Class

from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN = (By.ID, 'login')
    VERIFY_LOGIN = (By.XPATH, "//a[@id='account-sign-in']")

    #def enter_email(self, email):
    #self.input_text(*self.EMAIL)

    def enter_email(self,email):
        self.input_text(email,*self.EMAIL)
        #self.send_keys('samha1n@encouragesless.site')

    #def enter_email(self, email):
        #self.input_text(self, *self.EMAIL)

        #self.input_text(self,text'samha1n@encouragesless.site', *EMAIL)

    def enter_password(self, *PASSWORD):
        self.input_text('fhU6&Uavv?E*&7B', *self.PASSWORD)
        sleep(2)

    def enter_login(self):
        self.click(*self.LOGIN)
        sleep(2)

    def verify_login(self):
        #self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)
        self.verify_partial_text('Hi, tester', *self.VERIFY_LOGIN)
        sleep(2)


