from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_LINK = By.XPATH, "//a[@href= 'https://www.amazon.com/privacy']"


@given("Open Amazon T&C page")
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when("Store original windows")
def store_windows(context):
    context.original_window = context.driver.current_window_handle


@when("Click on Amazon Privacy link")
def click_on_privacy(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when("Switch to the newly opened window")
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])


@then("Verify Amazon Privacy Notice page is opened")
def verify_privacy_page_is_opened(context):
    context.driver.wait.until(EC.url_contains("https://www.amazon.com/gp/help/customer/"))


@then("User can close new window and switch back to original")
def close_window_and_switch(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)

