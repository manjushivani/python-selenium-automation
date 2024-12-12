from itertools import product
from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the target help page')
def open_target_help_page(context):
    context.driver.get('https://help.target.com/help')
    sleep(5)
@then('click on search help')
def click_on_search_help(context):
    context.driver.find_element(By.XPATH, "//input[@class='btn-sm search-btn']").click()
    sleep(5)
@then('verify search result page')
def verify_search_result_page(context):
    help_result_page=context.driver.find_elements(By.ID,
                                         'search_result_label')
    print('\nFind elements:')
    print(help_result_page)
    print(len(help_result_page))
