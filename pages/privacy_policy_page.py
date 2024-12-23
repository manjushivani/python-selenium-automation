from pages.base_page import BasePage


class PrivacyPolicyPage(BasePage):

    def verify_pp_opened(self):
        self.verify_partial_url('target-privacy-policy/')