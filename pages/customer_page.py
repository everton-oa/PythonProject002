from pages.base_page import BasePage
from locators.locators import Customer
from selenium.webdriver.common.by import By


class CustomerPage(BasePage):
    def __init__(self, init_browser):
        super().__init__(init_browser)
        self.USERSELECT_SELECT = (By.CSS_SELECTOR, Customer.USERSELECT_SELECT)
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, Customer.LOGIN_BUTTON)

    def select_user(self, user_name):
        self.select(self.USERSELECT_SELECT, user_name)

    def login(self):
        self.click(self.LOGIN_BUTTON)
