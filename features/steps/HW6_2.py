from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


SUBMENU = By.CSS_SELECTOR, "#zg_header li"


@then("All correct top links are opened")
def verify_best_sellers_top_links(context):
    all_submenu = context.driver.find_elements(*SUBMENU)
    number_of_elements = len(all_submenu)
    for i in range(number_of_elements):
        menu = context.driver.find_elements(*SUBMENU)[i]
        menu.click()
        submenu_title = context.driver.find_element(By.CSS_SELECTOR, "span#zg_banner_text").text
        menu_text = context.driver.find_elements(*SUBMENU)[i].text
        print(submenu_title)
        assert menu_text in submenu_title, "No text presented"
