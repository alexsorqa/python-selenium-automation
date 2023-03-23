from behave import given, then, when


@given("Opens Amazon page")
def open_amazon(context):
    context.app.main_page.open_main_url()


@when("Click Amazon Orders link")
def click_orders_link(context):
    context.app.main_page.click_orders()


@then("Verify Sign In page is opened")
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in()


@when("Clicks on Cart icon")
def click_cart_icon(context):
    context.app.header.click_cart()


@then("Verify 'Your Shopping Cart is empty.' text present")
def verify_cart_is_empty(context):
    context.app.cart_page.verify_cart_is_empty()


@when("Search for product")
def search_product(context):
    context.app.header.input_search_text("curry 8")
    context.app.header.click_search()


@then("Product results page is displayed")
def verify_results_page(context):
    context.app.product_results_page.verify_results_page()


@then("Click on first item")
def click_on_first_item(context):
    context.app.product_results_page.click_on_specific_item()


@then("Product page is displayed")
def verify_product_page(context):
    context.app.product_page.verify_product_page()


@when("Selects size")
def selects_size_and_add_to_cart(context):
    context.app.product_page.select_size()


@when("Add to Cart")
def add_to_cart(context):
    context.app.product_page.add_to_cart()


@then("Cart page is displayed")
def verify_cart_page(context):
    context.app.cart_page.verify_shopping_cart()





