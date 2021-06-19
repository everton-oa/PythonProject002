from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Browser:

    CHROME = 0
    FIFEFOX = 1

    def create_new_driver(driver_id):
        if Browser.CHROME == driver_id:
            print("\nInitiating ChromeDriver")
            driver = webdriver.Chrome()
        elif Browser.FF == driver_id:
            driver = webdriver.Firefox()
            print("\nInitiating GeckoDriver")
        return driver
