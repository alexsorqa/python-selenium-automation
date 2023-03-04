from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Click on water")
def verify_water(context):
    context.driver.find_element(By.XPATH, "//div[contains(text(), 'Sparkling ICE, Black Raspberry')]").click()


@then("Water page is shown")
def verify_water_page(context):
    context.driver.find_element(By.ID, "productTitle")


@then("Click on quantity")
def quantity_select(context):
    context.driver.find_element(By.ID, "a-autoid-0-announce").click()


@then("Select 3 items")
def quantity_select_items(context):
    context.driver.find_element(By.ID, "quantity_2").click()


@then("Click on Add to Cart")
def water_add_to_cart(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()
    sleep(3)


@then("Click on Cart icon")
def click_on_cart_icon(context):
    context.driver.find_element(By.ID, "nav-cart-count").click()


@then("3 items are added")
def verify_cart(context):
    context.driver.find_element(By.XPATH, "//a[@aria-label = '3 items in cart']")





