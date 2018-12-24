import pytest
from selene.browser import set_driver, driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(object):

    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        set_driver(webdriver.Chrome(ChromeDriverManager().install()))

        yield
        driver().quit()
