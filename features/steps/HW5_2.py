from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = By.CSS_SELECTOR, "#variation_color_name li"
COLORS = ['Black', 'Charcoal Heather', 'Light Grey Heather', 'Navy', 'Blue Heather', 'Burgundy', 'Olive Heather', 'Blue', 'Denim', 'Forest Green', 'Gold', 'Green, Abstract/Camo', 'Medium Brown', 'Nutmeg', 'Off-white', 'Pink', 'Purple', 'Toffee Brown', 'Light Grey', 'Red', 'Green, Camo', 'White']
CURRENT_COLOR = By.CSS_SELECTOR, "#variation_color_name .selection"


@when("Search for hoodie")
def search_hoodie(context):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("hoodie")
    context.driver.find_element(By.ID, "nav-search-submit-button").click()


@then("Select hoodie")
def select_hoodie(context):
    context.driver.find_element(By.XPATH, "//h2//a//span[contains(text(), 'Hooded Fleece')]").click()


@then("Hoodie page is displayed")
def display_hoodie_page(context):
    context.driver.wait.until(EC.url_contains("/Amazon-Essentials-Standard-Sweatshirt"), message='Invalid URL')


@then("All colors are presented")
def verify_colors(context):
    expected_colors = []
    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for color in all_color_options:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        expected_colors.append(current_color)
    assert COLORS == expected_colors, f"Some colors are missing"
