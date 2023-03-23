from selenium.webdriver.common.by import By
from pages.base_page import Page


class Cart(Page):

    EMPTY_CART = (By.XPATH, "//div//h2[contains(text(), 'Your Amazon Cart is empty')]")
    SHOPPING_CART = (By.CSS_SELECTOR, "div.a-row h1")

    def verify_cart_is_empty(self):
        assert self.find_element(*self.EMPTY_CART).text == 'Your Amazon Cart is empty', 'Cart is not empty'

    def verify_shopping_cart(self):
        assert self.find_element(*self.SHOPPING_CART).text == 'Shopping Cart', 'Wrong text is displayed'