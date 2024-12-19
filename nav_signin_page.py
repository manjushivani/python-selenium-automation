from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

NAV_SIGNIN = (By.XPATH, "//*[@data-test='accountNav-signIn']")

class NavPage(BasePage):

    def click_nav_signin(self):
        self.click(*self.NAV_SIGNIN)
        sleep(10)




