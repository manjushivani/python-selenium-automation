from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')
    sleep(5)

@when('Click on Cart icon')
def click_icon(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()


@then('Verify “Your cart is empty” message is shown')
def verify_cart_results(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    assert expected_result in  actual_result, f'Expected text {expected_result} not in actual {actual_result}'

@when('Click Sign In')
def click_signin(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()

@then('From right side navigation menu, click Sign In')
def click_signin(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

@then('Verify Sign In form opened')
def click_signin(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.XPATH, "//h1/span").text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'