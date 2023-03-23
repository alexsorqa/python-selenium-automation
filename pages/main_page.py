from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    ORDERS_ICON = (By.ID, "nav-orders")

    def open_main_url(self):
        self.open_url('https://www.amazon.com/')

    def click_orders(self):
        self.click(*self.ORDERS_ICON)
