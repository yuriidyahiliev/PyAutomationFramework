from selene.support.conditions import have

from src.pages.base_page import BasePage
from src.pages.search_page import SearchPage
from tests.base import BaseTest


class TestSearch(BaseTest):

    def test_user_can_search(self):
        BasePage.at(SearchPage())\
            .open()\
            .search("Selenium")\
            .get_search_results()\
            .should(have.size_at_least(1))
