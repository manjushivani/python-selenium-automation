from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle/')
    sleep(10)

@when('user click on circle page')
def open_target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-component='Cells Component Container'] [class='cell-item-content']").click()
    sleep(10)

@then('verify {expected_amount} benefit cells')
def open_target_circle_page(context, expected_amount):
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[data-component='Cells Component Container'] [class='cell-item-content']")
    print('\nFind elements:')
    print(cells)
    print(len(cells))

    #assert len(cells) == int(expected_amount), f'Expected {expected_amount} links but got {len(cells)}'

