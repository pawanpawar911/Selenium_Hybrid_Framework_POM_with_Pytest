#it requires the configparser

import configparser

config = configparser.RawConfigParser()  # there is class rawConfigparser in config parser to parse the data

config.read(".\\configuration\\config.ini")

class ReadConfig:
    @staticmethod  # don't need to use the self in def function
    def getWebURL():
        url = config.get('common info', 'base_url')
        return url
        
        
    @staticmethod  # don't need to use the self in def function
    def get_valid_usrName():
        valid_username = config.get('common info', 'valid_usrName')
        return valid_username
        
        
    @staticmethod  # don't need to use the self in def function
    def get_valid_passWord():
        valid_password = config.get('common info', 'valid_passWord')
        return valid_password
        
        
    @staticmethod  # don't need to use the self in def function
    def get_invalid_usrName():
        invalid_username = config.get('common info', 'invalid_usrName')
        return invalid_username
        
        
    @staticmethod  # don't need to use the self in def function
    def get_invalid_passWord():
        invalid_password = config.get('common info', 'invalid_passWord')
        return invalid_password
        