from selene import browser
from selene.support.jquery_style_selectors import s

from src.pages.base_page import BasePage
from src.pages.results_page import ResultsPage


class SearchPage(BasePage):

    def __init__(self):
        self.search_input = s("[name ='q']")

    def open(self, url='/'):
        browser.open_url(url)
        return self

    def search(self, search_value):
        self.search_input.set_value(search_value).press_enter()
        return ResultsPage()
