from pages.base_page import BasePage
from locators.locators import Customer, Account
from selenium.webdriver.common.by import By


class AccountPage(BasePage):
    def __init__(self, init_browser):
        super().__init__(init_browser)
        self.WELCOME_USER_NAME = (By.CSS_SELECTOR, Account.WELCOME_USER_NAME)

    def get_welcome_username(self):
        return self.get_element_text(self.WELCOME_USER_NAME)
