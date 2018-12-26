from typing import TypeVar

from src.utils.config_parser import get_config_by_key


class BasePage(object):

    T = TypeVar("T")

    @staticmethod
    def at(self: T) -> T:
        return self

    @staticmethod
    def get_base_url():
        return get_config_by_key('ui', 'url')

    def then(self):
        return self

