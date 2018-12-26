import yaml


def get_config_by_key(first_key, second_key):
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        return cfg[first_key][second_key]


class ConfigParser:
    pass
