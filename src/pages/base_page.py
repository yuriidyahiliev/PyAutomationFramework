from typing import TypeVar

from src.utils.config_parser import ConfigParser


class BasePage(object):

    T = TypeVar("T")

    @staticmethod
    def at(self: T) -> T:
        return self

    base_url = ConfigParser().get_config_by_key('UI', 'BASE_URL')

    def then(self):
        return self

