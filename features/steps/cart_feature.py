from itertools import product
from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

@then('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart(cart=CART_ICON)

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()
    #expected_result = 'Your cart is empty'
    #actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    #assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'

