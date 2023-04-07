from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class Header(Page):

    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CART_ICON = (By.ID, 'nav-cart-count-container')
    DEPARTMENT_SELECTION = (By.ID, "searchDropdownBox")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def select_department(self, alias):
        if alias == 'Video Games':
            alias = 'videogames'
        department_dd = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_dd)
        select.select_by_value(f'search-alias={alias}')
