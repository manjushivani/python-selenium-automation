from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


from behave import given, when, then
from time import sleep


NAV_SIGNIN = (By.XPATH, "//*[@data-test='accountNav-signIn']")
EMAIL = (By.ID, 'username')
PASSWORD = (By.ID, 'password')
LOGIN = (By.ID, 'login')
VERIFY_LOGIN = (By.XPATH, "//a[@id='account-sign-in']")


# Open target.com
@given('Open target main page  # main page')
def open_target_main_page(context):
    context.app.main_page.open_main()

@when('Click Sign In  # header')
def click_account_login(context):
    #context.driver.find_element(*SIGN_IN).click()
    context.app.header.click_sign_in()
    sleep(5)

@then('From right side navigation menu, click Sign In # header or create PO for menu')
def click_side_nav_sign_in(context):
    #context.driver.find_element(*NAV_SIGNIN).click()
    context.app.header.click_nav_signin()
    sleep(5)

@then('Verify Sign In form opened # sign in page')
def verify_sign_in_form(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.XPATH, "//h1/span").text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'

@then('enter email address')
def enter_email(context):
    #context.driver.find_element(*EMAIL).send_keys('samha1n@encouragesless.site')
    context.app.login_page.enter_email('samha1n@encouragesless.site')

@then('enter password')
def enter_password(context):
    #context.driver.find_element(*PASSWORD).send_keys('fhU6&Uavv?E*&7B')
    context.app.login_page.enter_password()

@then('click on sign in button')
def click_sign_in_button(context):
    #context.driver.find_element(*LOGIN).click()
    context.app.login_page.enter_login()
    sleep(10)

#@then('click on next button')
#def click_skip_button(context):
    #context.driver.find_element(By.XPATH, "//a[text()='Skip']").click()
    #sleep(5)

#@then('click on May be later button')
#def click_maybe_button(context):
    #context.driver.find_element(By.XPATH, "//button[text()='Maybe later']").click()
    #sleep(5)


@then('verify user is logged in')
def verify_user(context):
    #ex_result = 'Hi, tester'
    #actual_result = context.driver.find_element(*VERIFY_LOGIN).text
    #assert ex_result in actual_result, f'Expected {ex_result}, got {actual_result}'
    context.app.login_page.verify_login()










# OR:
#driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")

# Make sure login button is shown
#driver.find_element(By.ID, 'login')