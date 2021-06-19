from tests.test_base import BaseTest
from pages.home_page import HomePage
from pages.customer_page import CustomerPage
import time


class TestHomePage(BaseTest):
    def test_valid_login(self):
        self.home_page = HomePage(self.driver)
        self.home_page.open_home_page()
        self.home_page.click_customer_login_button()
        import pdb

        pdb.set_trace()
        self.customer_page = CustomerPage(self.driver)
        time.sleep(1)
