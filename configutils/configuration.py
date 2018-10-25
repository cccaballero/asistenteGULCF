import configparser

from utils.singelton import Singleton
from .configstorage import ConfigStorage


@Singleton
class Configuration:

    def __init__(self, config_file='app.cfg'):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    @staticmethod
    def _parse_params(params):
        """
        Parse configuration entries and converts to Python types
        :param params: Configuration storage object
        :type params: ConfigStorage
        :return: Configuration storage object including python types
        :rtype: ConfigStorage
        """
        for key, value in params.items():
            if value.lower() in ('none', 'null', ''):
                params[key] = None
            elif value.lower() == 'true':
                params[key] = True
            elif value.lower() == 'false':
                params[key] = False
            elif value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
                params[key] = int(value)
            elif ',' in value:
                params[key] = list(map(lambda x: x.strip(), value.split(',')))
            else:
                try:
                    params[key] = float(value)
                except:
                    pass
        return params

    def get_section_config(self, section):
        """
        Return params from specified configuration section
        :param section: Configuration section name
        :type section: str
        :return: Configuration params
        :rtype: ConfigStorage
        """
        params = self._parse_params(ConfigStorage(self.config[section]))
        return params

    def get_main_params(self):
        """
        Return params from main configuration section
        :return: Configuration params
        :rtype: ConfigStorage
        """
        return self.get_section_config('main')

    def get_sender_params(self):
        """
        Return params from sender configuration section
        :return: Configuration params
        :rtype: ConfigStorage
        """
        return self.get_section_config('sender')

    def get_receiver_params(self):
        """
        Return params from receiver configuration section
        :return: Configuration params
        :rtype: ConfigStorage
        """
        return self.get_section_config('receiver')

    def get_db_params(self):
        """
        Return params from db configuration section
        :return: Configuration params
        :rtype: ConfigStorage
        """
        return self.get_section_config('db')
