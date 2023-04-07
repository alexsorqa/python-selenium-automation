from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class ProductPage(Page):

    ADD_TO_CART = (By.ID, "add-to-cart-button")
    SIZES = (By.ID, "dropdown_selected_size_name")
    SIZES_MENU = (By.CSS_SELECTOR, "div.a-popover-wrapper li")
    NEW_ARRIVALS = (By.XPATH, "//span[@class= 'nav-a-content' and contains(text(), 'New Arrivals')]")
    NEW_DEALS = (By.XPATH, "//ul[@class='mm-category-list']/li[contains(text(), 'See More')]")

    def verify_product_page(self):
        self.find_element(*self.ADD_TO_CART)

    def select_size(self):
        self.click(*self.SIZES)
        sleep(1)
        size_9 = self.find_elements(*self.SIZES_MENU)[10]
        size_9.click()
        sleep(3)

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)
        sleep(4)

    def open_cat_hoodie_page(self):
        self.open_url("https://www.amazon.com/gp/product/B074TBCSC8")

    def hover_over_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_deals_displayed(self):
        all_deals = self.find_elements(*self.NEW_DEALS)
        self.wait_for_element_appear(*self.NEW_DEALS)
        if len(all_deals) == 6:
            return True





