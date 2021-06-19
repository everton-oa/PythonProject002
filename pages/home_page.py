from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, init_browser):
        super().__init__(init_browser)

    def open_home_page(self):
        self.open_url("https://www.way2automation.com/angularjs-protractor/banking/")
