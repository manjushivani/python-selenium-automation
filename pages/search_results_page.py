from selenium.webdriver.common.by import By
from time import sleep

from pages import cart_page
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")


    def verify_search_results(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULTS).text
        assert product in actual_result, f'Expected text {product} not in actual {actual_result}'

