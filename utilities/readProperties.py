from Configurations.configurations import *


class ReadConfig:
    def get_url(self):
        return common_info['baseURL']

    def get_username(self):
        return common_info['username']

    def get_password(self):
        return common_info['password']
