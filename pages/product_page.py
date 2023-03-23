from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ProductPage(Page):

    ADD_TO_CART = (By.ID, "add-to-cart-button")
    SIZES = (By.ID, "dropdown_selected_size_name")
    SIZES_MENU = (By.CSS_SELECTOR, "div.a-popover-wrapper li")

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

