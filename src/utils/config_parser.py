import configparser
import json


class ConfigParser:
    file_name = 'config.json'

    def __init__(self):
        self.config = configparser.ConfigParser()

    def get_config_by_key(self, first_key, second_key):
        with open(self.file_name, 'r') as f:
            self.config = json.load(f)

        return self.config[first_key][second_key]
