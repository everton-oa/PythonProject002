from pages.base_page import BasePage
from locators.locators import Home
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, init_browser):
        super().__init__(init_browser)
        self.CUSTOMER_LOGIN_BOTTON = (By.CSS_SELECTOR, Home.CUSTOMER_LOGIN_BOTTON)
        self.BANK_MANAGER_LOGIN_BUTTON = (
            By.CSS_SELECTOR,
            Home.BANK_MANAGER_LOGIN_BUTTON,
        )

    def open_home_page(self):
        self.open_url("https://www.way2automation.com/angularjs-protractor/banking/")

    def click_customer_login_button(self):
        self.click(self.CUSTOMER_LOGIN_BOTTON)
