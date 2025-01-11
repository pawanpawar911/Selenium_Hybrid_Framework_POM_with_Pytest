import logging
import os

class LogGenerate:
    @staticmethod
    def logger_file():
            
        logging.basicConfig(filename = ".\\logs\\test.log", format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%d-%m-%Y %H:%M:%S', force=True)
        
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger