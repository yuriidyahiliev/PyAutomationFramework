import unittest

from selene import browser, config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src.utils.config_parser import get_config_by_key

desired_cap = {'browserName': 'chrome',
               'version': '69.0',
               'enableVNC': True,
               'javascriptEnabled': True}


class BaseTest(unittest.TestCase):
    TIMEOUT = 10

    config.base_url = get_config_by_key("ui", "url")
    config.timeout = TIMEOUT

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--start-maximized")
        # For remote test execution

        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--disable-notifications")
        # chrome_options.add_argument("--enable-automation")
        # chrome_options.add_argument("--start-maximized")
        #
        # driver = webdriver.Remote(
        #     command_executor='http://127.0.0.0.1:4444/wd/hub',
        #     desired_capabilities=desired_cap)

        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)

        browser.set_driver(cls.driver)

    @classmethod
    def tearDownClass(cls):
        browser.quit()
