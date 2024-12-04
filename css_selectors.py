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



# CSS
#driver.find_element(By.ID, "twotabsearchtextbox")
# CSS, by id:
#driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
# CSS, by id & tag
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
# CSS, by class
driver.find_element(By.CSS_SELECTOR, '.nav-progressive-attribute')
driver.find_element(By.CSS_SELECTOR, '.nav-progressive-attribute.nav-input')
# CSS, by tag and class
driver.find_element(By.CSS_SELECTOR, 'input.nav-progressive-attribute.nav-input')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox.nav-progressive-attribute.nav-input')

# CSS, by attributes
driver.find_element(By.CSS_SELECTOR, "[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id='nav_cs_bestsellers']")

# by CSS, attr partial match => *=
driver.find_element(By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']")
# keep in mind, you can access class as attributes:
driver.find_element(By.CSS_SELECTOR, "[class*='styles_baseCell'][class*='styles_cellSkinny']")

# By CSS selector, from parent node => to child
driver.find_element(By.CSS_SELECTOR, "[data-module-type='ProductListGrid'] h2")


# Lesson 3 homework for Amazon CSS selector
# 1. Locator for Amazon logo
#CSS, by class
driver.find_element(By.CSS_SELECTOR, "[href='/ref=ap_frn_logo']")

#2. for create account
#CSS, by tag and class
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#3. CSS, by ID for your name
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#4 CSS, by ID for email
driver.find_element(By.CSS_SELECTOR, '##ap_email')

#5 CSS, by ID for Password
driver.find_element(By.CSS_SELECTOR, '##ap_password')

#6 CSS, by ID for password check
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#7 CSS, by ID for continue button
driver.find_element(By.CSS_SELECTOR, '#continue')

#8 CSS, by partial match
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_condition_of_use']")

#9 CSS, by partial match
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_privacy_notice']")

#10 CSS, by class for signin
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')

