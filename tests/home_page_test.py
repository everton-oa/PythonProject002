from tests.test_base import BaseTest
from pages.home_page import HomePage
import time


class TestHomePage(BaseTest):
    def test_001(self):
        self.home_page = HomePage(self.driver)
        self.home_page.open_home_page()
        time.sleep(1)
