##from itertools import product
##from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

#SEARCH_FIELD = (By.ID, 'search')
#SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
LISTINGS = (By.CSS_SELECTOR, "[data-test*='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")


@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()

@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)
    #context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    #context.driver.find_element(*SEARCH_BTN).click()
    #sleep(10)

@when('Click on Add to Cart button')
def target_click_add_to_cart(context):
    context.app.cart_page.add_to_cart()
    #context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
    #context.driver.find_elements(By.CSS_SELECTOR, "[id*='addToCartButton']")[0].click()
    #context.driver.wait.until(EC.visibility_of_element_located(ADD_TO_CART_BTN))
    sleep(10)

@when('Store product name')
def target_store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')
    sleep(10)

@when('Confirm Add to Cart button from side navigation')
def target_side_nav_click_add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_SIDE_NAV_BTN)).click()
    #context.driver.find_element(*ADD_TO_CART_SIDE_NAV_BTN).click()


@when('Verify search results shown')
def search_product(context):
    context.driver.find_element(By.XPATH, "//div[@class='h-display-flex']")
    sleep(10)

@then('Verify search results shown for {product}')
def verify_search_results(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected text {product} not in actual {actual_result}'
    sleep(10)

@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')
    sleep(10)


@when('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]").text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"
    sleep(10)


@when('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
    print(f'Actual product in cart name: {actual_name}')
    print(f'Product name stored earlier: {context.product_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"
    sleep(10)

@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    # Find all products:
    all_products = context.driver.find_elements(*LISTINGS)
    # print(all_products)
    assert len(all_products) > 0, 'No products found'

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title != '', 'Product title not shown'
        # print(title)
        product.find_element(*PRODUCT_IMG)