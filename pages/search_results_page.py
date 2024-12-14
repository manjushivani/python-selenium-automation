from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")
    EMPTY_CART =  (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")


    def verify_search_results(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULTS).text
        assert product in actual_result, f'Expected text {product} not in actual {actual_result}'

    def verify_cart_empty(self, product):
        expected_result = 'Your cart is empty'
        actual_result = self.find_element(*self.EMPTY_CART).text
        assert product == actual_result, f'Expected {expected_result} did not match actual {actual_result}'