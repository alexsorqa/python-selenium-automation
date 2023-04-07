from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Results(Page):

    PRODUCT_RESULTS = (By.CSS_SELECTOR, ".a-price-whole")
    RESULTS_TEXT = (By.XPATH, "//div[@cel_widget_id='MAIN-TOP_BANNER_MESSAGE-1']//span[contains(text(), 'RESULTS')]")
    SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")

    def get_subnav_locator(self, category):
        return [self.SUBNAV[0], self.SUBNAV[1].replace('{CATEGORY}', category)]

    def verify_results_page(self):
        self.find_element(*self.RESULTS_TEXT)

    def click_on_specific_item(self):
        all_product_results = self.driver.find_elements(*self.PRODUCT_RESULTS)[0]
        all_product_results.click()
        sleep(5)

    def verify_selected_department(self, category):
        locator = self.get_subnav_locator(category)
        print(locator)
        self.wait_for_element_appear(*locator)



