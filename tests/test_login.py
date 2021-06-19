from pages.account_page import AccountPage
from tests.test_base import BaseTest
from pages.home_page import HomePage
from pages.customer_page import CustomerPage
import time


class TestHomePage(BaseTest):
    def test_valid_login(self):
        self.home_page = HomePage(self.driver)
        self.home_page.open_home_page()
        self.home_page.click_customer_login_button()
        self.customer_page = CustomerPage(self.driver)
        self.customer_page.select_user("Harry Potter")
        self.customer_page.login()
        self.account_page = AccountPage(self.driver)
        # assert self.account_page.get_welcome_username == "Harry Potter"
        time.sleep(1)
