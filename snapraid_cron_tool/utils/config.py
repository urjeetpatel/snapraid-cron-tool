# Code from: https://medium.com/@unpluggedcoder/python-config-parser-compatible-with-environment-variable-8c5c46145a46
import os
import configparser


class Config:
    """Get config from config file or environment variables.
    The priority order of config is: Config file > Environment > default_value.
    The env var is composed by: [SECTION]_[OPTION]
    For example:
    get_or_else('smtp', 'BIND_ADDRESS', '127.0.0.1')
    => os.environ.get('SMTP_BIND_ADDRESS', '127.0.0.1')
    """

    config = configparser.ConfigParser()

    BOOLEAN_STATES = {
        "1": True,
        "yes": True,
        "true": True,
        "on": True,
        "0": False,
        "no": False,
        "false": False,
        "off": False,
    }

    @staticmethod
    def init_config(file):
        if file and os.path.exists(file):
            Config.config.read([file])

    @staticmethod
    def get_or_else(section, option, default_value):
        if Config.config.has_option(section, option):
            return Config.config.get(section, option, fallback=default_value)
        else:
            return os.environ.get("_".join([section.upper(), option]), default_value)

    @staticmethod
    def getint_or_else(section, option, default_value):
        if Config.config.has_option(section, option):
            return Config.config.getint(section, option, fallback=default_value)
        else:
            return Config._get_conv_env_or_else(section, option, int, default_value)

    @staticmethod
    def getfloat_or_else(section, option, default_value):
        if Config.config.has_option(section, option):
            return Config.config.getfloat(section, option, fallback=default_value)
        else:
            return Config._get_conv_env_or_else(section, option, float, default_value)

    @staticmethod
    def getboolean_or_else(section, option, default_value):
        if Config.config.has_option(section, option):
            return Config.config.getboolean(section, option, fallback=default_value)
        else:
            return Config._get_conv_env_or_else(section, option, Config._convert_to_boolean, default_value)

    @staticmethod
    def _get_conv_env_or_else(section, option, conv, default_value):
        return conv(os.environ.get("_".join([section.upper(), option.upper()]), default_value))

    @staticmethod
    def _convert_to_boolean(value):
        """Return a boolean value translating from other types if necessary."""
        if value.lower() not in Config.BOOLEAN_STATES:
            raise ValueError("Not a boolean: %s" % value)
        return Config.BOOLEAN_STATES[value.lower()]
