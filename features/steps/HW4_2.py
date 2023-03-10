from selenium.webdriver.common.by import By
from behave import given, when, then
<<<<<<< HEAD
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART = (By.ID, "add-to-cart-button")
WATER = (By.XPATH, "//div[contains(text(), 'Sparkling ICE, Black Raspberry')]")
=======
from time import sleep
>>>>>>> ee43ac350a6216d68391d8c38be3f8a15db9a7d2


@then("Click on water")
def verify_water(context):
<<<<<<< HEAD
    context.driver.wait.until(EC.element_to_be_clickable(WATER), message="Item is not displayed").click()
=======
    context.driver.find_element(By.XPATH, "//div[contains(text(), 'Sparkling ICE, Black Raspberry')]").click()
>>>>>>> ee43ac350a6216d68391d8c38be3f8a15db9a7d2


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
<<<<<<< HEAD
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART)).click()
=======
    context.driver.find_element(By.ID, "add-to-cart-button").click()
    sleep(3)
>>>>>>> ee43ac350a6216d68391d8c38be3f8a15db9a7d2


@then("Click on Cart icon")
def click_on_cart_icon(context):
    context.driver.find_element(By.ID, "nav-cart-count").click()


@then("3 items are added")
def verify_cart(context):
    context.driver.find_element(By.XPATH, "//a[@aria-label = '3 items in cart']")





