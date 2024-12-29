import logging
import os

class LogGenerate:
    @staticmethod
    def logger_file():
        # log_dir = "logs"
        # os.makedirs(log_dir, exist_ok=True)
        
        # # Define the log file path
        # log_file = os.path.join(log_dir, "test_log_file.log")
        
        # # Check if the log file exists, create an empty one if not
        # if not os.path.exists(log_file):
        #     open(log_file, 'w').close()  # Create an empty file
            
        logging.basicConfig(filename = ".\\logs\\test.log", format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%d-%m-%Y %H:%M:%S', force=True)
        
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        #logger.propagate = False
        return logger