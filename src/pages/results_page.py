from selene import browser
from selene.support.jquery_style_selectors import ss

from src.pages.base_page import BasePage


class ResultsPage(BasePage):

    def __init__(self):
        self.search_results = ss("a > h3")

    def open(self):
        browser.open_url("/search")

    def get_search_results(self):
        return self.search_results
