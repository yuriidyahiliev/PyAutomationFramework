import pytest
from selene import config, browser
from selene.browser import set_driver, driver
from selene.browsers import BrowserName
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

desired_cap = {'browserName': 'chrome',
               'version': '69.0',
               'enableVNC': True,
               'javascriptEnabled': True}


class BaseTest(object):

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

        driver = webdriver.Chrome(ChromeDriverManager().install())

        browser.set_driver(driver)
        yield
        browser.quit()
