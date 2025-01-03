from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class HelpPage(BasePage):
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER_TXT = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
    HELP_DD = (By.CSS_SELECTOR, "[id*='ViewHelpTopics']")

    # Dynamic locator
    def _get_header_locator(self, text):
        # HEADER_TXT = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
        # => HEADER_TXT = (By.XPATH, "//h1[text()=' Returns']")
        return [self.HEADER_TXT[0], self.HEADER_TXT[1].replace('{SUBSTRING}', text)]

    def open_help_returns(self):
        self.open_url('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_promotions(self, dd_option_value):
        dropdown = self.find_element(*self.HELP_DD)
        select = Select(dropdown)
        select.select_by_value(dd_option_value)

    def verify_hep_topic_opened(self, selected_header):
        locator = self._get_header_locator(selected_header)
        self.wait_for_element_visible(*locator)

    def verify_returns_opened(self):
        self.wait_for_element_visible(*self.HEADER_RETURNS)

    def verify_promotions_opened(self):
         self.wait_for_element_visible(*self.HEADER_PROMOTIONS)

