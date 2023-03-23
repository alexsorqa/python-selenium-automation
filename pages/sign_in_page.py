from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignIn(Page):
    SIGN_IN = (By.XPATH, "//h1[@class = 'a-spacing-small' and contains(text(), 'Sign in')]")

    def verify_sign_in(self):
        self.find_element(*self.SIGN_IN)