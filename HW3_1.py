from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= "C:/Users/bonum/Desktop/python-selenium-automation/chromedriver.exe")

amazon_logo = driver.find_element(By.CSS_SELECTOR, 'a.a-link-nav-icon')
create_account = driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
your_name = driver.find_element(By.CSS_SELECTOR, "input[autocomplete = 'name']")
email = driver.find_element(By.CSS_SELECTOR, "input#ap_email")
password = driver.find_element(By.CSS_SELECTOR, "input#ap_password")
password_requirements = driver.find_element(By.CSS_SELECTOR, "div.a-box.a-alert-inline.a-alert-inline-info.auth-inlined-information-message.a-spacing-top-mini")
password_verify = driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
continue_button = driver.find_element(By.CSS_SELECTOR, "input#continue")
conditions_of_use = driver.find_element(By.CSS_SELECTOR, "a[href*= 'condition_of_use']")
privacy_notice = driver.find_element(By.CSS_SELECTOR, "a[href*= 'ap_register_notification_privacy_notice']")
sign_in = driver.find_element(By.CSS_SELECTOR, "a[href*= '/ap/signin?openid']")

