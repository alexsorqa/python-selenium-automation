from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= "C:/Users/bonum/Desktop/python-selenium-automation/chromedriver.exe")

amazon_logo = driver.find_element(By.XPATH, "//i[@class = 'a-icon a-icon-logo' and @role = 'img']")
email_field = driver.find_element(By.ID, "ap_email")
continue_button = driver.find_element(By.XPATH, "//input[@tabindex = '5']")
need_help_link = driver.find_element(By.XPATH, "//span[@class = 'a-expander-prompt']")
forgot_password_link = driver.find_element(By.ID, "auth-fpp-link-bottom")
other_issues_link = driver.find_element(By.XPATH, "//a[@class = 'a-link-normal' and contains(@href, 'account-issues')]")
create_amazon_account = driver.find_element(By.XPATH, "//a[@class = 'a-button-text' and contains(href, '')]")
conditions_link = driver.find_element(By.XPATH, "//a[@class = 'a-link-normal' and contains(text(), 'Conditions of Use')]")
privacy_notice_link = driver.find_element(By.XPATH, "//a[@rel = 'noopener' and contains(text(), 'Privacy Notice')]")






