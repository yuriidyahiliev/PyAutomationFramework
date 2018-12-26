import pytest
from selene import browser, config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src.utils.config_parser import get_config_by_key

desired_cap = {'browserName': 'chrome',
               'version': '69.0',
               'enableVNC': True,
               'javascriptEnabled': True}


class BaseTest(object):

    config.base_url = get_config_by_key("ui", "url")

    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--disable-notifications")
        # chrome_options.add_argument("--enable-automation")
        # chrome_options.add_argument("--start-maximized")
        #
        # driver = webdriver.Remote(
        #     command_executor='http://127.0.0.0.1:4444/wd/hub',
        #     desired_capabilities=desired_cap)

        # For remote test execution

        driver = webdriver.Chrome(ChromeDriverManager().install())

        browser.set_driver(driver)
        yield
        browser.quit()
