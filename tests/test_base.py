from pytest import mark


@mark.usefixtures("init_browser")
class BaseTest:
    pass
