from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Click on Best sellers")
def click_best_sellers(context):
    context.driver.find_element(By.XPATH, "//a[@href = '/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()
    sleep(2)


@then("5 submenus are displayed")
def verify_best_sellers_submenus(context):
    best_sellers = context.driver.find_elements(By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs-li-selected-div__3tHnP")
    submenus = context.driver.find_elements(By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR")
    count = (len(best_sellers) + len(submenus))
    print(f"{count} submenus are displayed")
    assert 5 == count, f"Expected: 5 submenus should be displayed, {count} are shown instead"
    ###Couldn't concatenate 5 submenus into one element...
