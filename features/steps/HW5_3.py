from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

ICE_CREAM_IMAGES = By.CSS_SELECTOR, "div.a-section.a-spacing-base span[data-component-type='s-product-image']"
ALL_ELEMENTS = By.CSS_SELECTOR, "div.s-widget-container"
ICE_CREAM_TITLES = By.CSS_SELECTOR, "div.a-section h2 span.a-size-base-plus"


@when("Ice Cream search")
def search_ice_cream(context):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("ice cream")
    context.driver.find_element(By.ID, "nav-search-submit-button").click()


@then("All items have Images and Titles")
def verify_images_and_titles(context):
    total_images = context.driver.find_elements(*ICE_CREAM_IMAGES)#[:3]
    total_titles = context.driver.find_elements(*ICE_CREAM_TITLES)#[:3]
    arr = []
    for image in total_images:
        if image not in total_images:
            print("No image is displayed")
            break
        else:
            arr.append(1)

    for title in total_titles:
        if title not in total_titles:
            print("No title is displayed")
            break
        else:
            arr.append(2)

    image_count, title_count = arr.count(1), arr.count(2)

    print(image_count, title_count)
    assert image_count == title_count, f"Some images or titles are missing"

