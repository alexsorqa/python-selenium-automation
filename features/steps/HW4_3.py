from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Amazon Customer Service")
def open_amazon_customer_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@then("Customer service UI is presented")
def verify_customer_service_ui(context):
    context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Welcome to Amazon')]")
    context.driver.find_elements(By.CSS_SELECTOR, "div.issue-card-wrapper")
    context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Search our help library')]")
    context.driver.find_element(By.ID, "hubHelpSearchInput")
    context.driver.find_element(By.XPATH, "//h2[contains(text(), 'All help topics')]")
    context.driver.find_elements(By.CSS_SELECTOR, "li.help-topics")