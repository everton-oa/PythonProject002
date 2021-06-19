from pages.browser_manager import Browser
from pytest import fixture


@fixture(scope="class")
def init_browser(request):
    web_driver = Browser.create_new_driver(Browser.CHROME)
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.close()
    web_driver.quit()
