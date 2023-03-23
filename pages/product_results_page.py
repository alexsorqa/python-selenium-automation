from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Results(Page):

    PRODUCT_RESULTS = (By.CSS_SELECTOR, ".a-price-whole")
    RESULTS_TEXT = (By.XPATH, "//div[@cel_widget_id='MAIN-TOP_BANNER_MESSAGE-1']//span[contains(text(), 'RESULTS')]")

    def verify_results_page(self):
        self.find_element(*self.RESULTS_TEXT)

    def click_on_specific_item(self):
        all_product_results = self.driver.find_elements(*self.PRODUCT_RESULTS)[0]
        all_product_results.click()
        sleep(5)

