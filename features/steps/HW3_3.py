from selenium.webdriver.common.by import By
from behave import given, when, then


@when("Click on Cart icon")
def click_cart(context):
    context.driver.find_element(By.ID, "nav-cart-count-container").click()


@then("Amazon cart page is displayed")
def amazon_cart_page(context):
    context.driver.get("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")


@then("Your Amazon Cart is empty text shown")
def verify_amazon_cart(context):
    amazon_cart_text = context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty").text
    assert amazon_cart_text == "Your Amazon Cart is empty", f"{amazon_cart_text} is displayed. Should be: 'Your Amazon Cart is empty'"