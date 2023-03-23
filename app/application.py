from pages.base_page import Page
from pages.main_page import MainPage
from pages.header import Header
from pages.sign_in_page import SignIn
from pages.cart_page import Cart
from pages.product_results_page import Results
from pages.product_page import ProductPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(self.driver)
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.cart_page = Cart(self.driver)
        self.product_results_page = Results(self.driver)
        self.product_page = ProductPage(self.driver)
