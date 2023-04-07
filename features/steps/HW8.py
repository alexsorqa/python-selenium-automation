from behave import given, then, when


@when("Select department by alias {alias}")
def select_one_department(context, alias):
    context.app.header.select_department(alias)


@when("Input text {text}")
def input_text_new_world(context, text):
    context.app.header.input_search_text("New World")


@when("Clicks on search icon")
def click_on_search_icon(context):
    context.app.header.click_search()


@then("Verify {category} department is selected")
def verify_video_games(context, category):
    context.app.product_results_page.verify_selected_department(category)


@given("Opens Cat Hoodie page")
def open_cat_hoodie_page(context):
    context.app.product_page.open_cat_hoodie_page()


@when("User hovers over New Arrivals")
def hover_over_new_arrivals(context):
    context.app.product_page.hover_over_new_arrivals()


@then("6 deals are displayed")
def deals_are_displayed(context):
    context.app.product_page.verify_deals_displayed()
