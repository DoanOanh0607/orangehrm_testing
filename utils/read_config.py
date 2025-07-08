import os
import json

class ConfigReader:
    _config = None

    @staticmethod
    def load_config():
        if ConfigReader._config is None:
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'testsetting.json')
            with open(config_path, 'r') as config_file:
                ConfigReader._config = json.load(config_file)
        return ConfigReader._config

    @staticmethod
    def get_url():
        return ConfigReader.load_config()['url']
    
    @staticmethod
    def get_username():
        return ConfigReader.load_config()['username']   
    
    @staticmethod
    def get_password():
        return ConfigReader.load_config()['password']
    
    @staticmethod
    def get_timeout():
        return ConfigReader.load_config()['timeout']
    
    @staticmethod
    def get_vacancy():
        return ConfigReader.load_config().get('vacancy', {})
    
    @staticmethod
    def get_newuser():
        return ConfigReader.load_config().get('newuser', {})
    

    
    
    
    

    
    
    


    


    