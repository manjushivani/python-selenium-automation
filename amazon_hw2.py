from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
#driver.get('https://www.amazon.com/')
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# XPath for the Amazon logo

# Locate the Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Locate the email field
driver.find_element(By.ID, 'ap_email').send_keys('manjuk25@hotmail.com') # Using ID locator

# Locate the Continue button
driver.find_element(By.ID, 'continue').click() # Using ID locator

# Locate the "Conditions of use" link
driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use')]")


# Locate the Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Notice')]")

#Locate Need help link
#driver.find_element("xpath", "//span[(text(), 'Need help?')]")

#Locate Need help link
#driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#locate Forgot your password?
driver.find_element(By.ID,'auth-fpp-link-bottom')

#Locate More ways to get support
sleep(5)
#driver.find_element(By.ID,'ap-other-signin-issues-link')
#driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")
driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/account-issues/ref=ap_login_with_otp_claim_collection?ie=UTF8']")

#locate Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')





