from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Amazon page")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(1)
    context.driver.maximize_window()


@when("Click orders")
def click_orders(context):
    context.driver.find_element(By.ID, "nav-orders").click()
    sleep(1)


@then("Sign in page is displayed")
def verify_sign_in_page(context):
    context.driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&accountStatusPolicy=P1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Forder-history%3Fie%3DUTF8%26ref_%3Dnav_orders_first&pageId=webcs-yourorder&showRmrMe=1")


@then("Sign In header is visible")
def verify_sign_in_header(context):
    header = context.driver.find_element(By.XPATH, "//h1[@class = 'a-spacing-small']").text
    assert header == "Sign in", f"{header} is visible instead of 'Sign In'"


@then("Email input field is present")
def verify_sign_in_email(context):
    context.driver.find_element(By.ID, "ap_email").click()
    sleep(1)