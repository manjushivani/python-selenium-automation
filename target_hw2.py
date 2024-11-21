from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')

# sign in
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
sleep(5)

#driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

sleep(5)
# Verification:
#driver.find_element(By.XPATH, "//button[click()='Sign In']")
ex_sign_result = 'Sign into your Target account'
actual_result_sgn = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
assert ex_sign_result in actual_result_sgn, f'expected {ex_sign_result} result in actual result {actual_result_sgn}'
print('Test case passed')

sleep(5)


driver.get('https://www.target.com/')
# Search
driver.find_element(By.ID, 'search').send_keys('shoes')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(5)

# Verification:
expected_result = 'shoes'
actual_result = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text

assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
print('Test case passed')

# Verify an element present:
driver.find_element(By.XPATH, "//*[text()='Quickly find what you need']")

