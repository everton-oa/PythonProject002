from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, init_browser):
        self.driver = init_browser

    def get_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )

    def open_url(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def click(self, by_locator):
        self.get_element(by_locator).click()

    def send_keys(self, by_locator, value):
        self.clear_input_field(by_locator)
        self.get_element(by_locator).send_keys(value)

    def clear_input_field(self, by_locator):
        self.get_element(by_locator).clear()

    def get_element_text(self, by_locator):
        element = self.get_element(by_locator)
        return element.text

    def is_enabled(self, by_locator):
        element = self.get_element(by_locator)
        return bool(element)

    def select(self, by_locator, value):
        select = Select(self.get_element(by_locator))
        return select.select_by_visible_text(value)
