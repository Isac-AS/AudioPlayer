import glob
import logging
import json
from os import mkdir

def init_logging_config():
    logging.basicConfig(filename="./logs/info_logs.txt", filemode="a" , format='%(asctime)s - [%(levelname)s]: %(message)s', level=logging.INFO)
    logging.basicConfig(filename="./logs/debug_logs.txt", filemode="a" , format='%(asctime)s - [%(levelname)s]: %(message)s', level=logging.DEBUG)
    logging.basicConfig(filename="./logs/warning_logs.txt", filemode="a" , format='%(asctime)s - [%(levelname)s]: %(message)s', level=logging.WARNING)
    logging.basicConfig(filename="./logs/error_logs.txt", filemode="a" , format='%(asctime)s - [%(levelname)s]: %(message)s', level=logging.ERROR)
    logging.basicConfig(filename="./logs/critical_logs.txt", filemode="a" , format='%(asctime)s - [%(levelname)s]: %(message)s', level=logging.CRITICAL)


def check_log_files():
    """
    Will check for the logs subdirectory.
    If it doesn't exist, it will be created along with the log files.
    """
    if glob.glob('logs'):
        init_logging_config()
        return True
    try:
        mkdir("./logs")
        init_logging_config()
        logging.info("Log files created successfully.")
        return True
    except Exception as e:
        logging.error("Problem with log file creation.")
        logging.error(e)
        return False

def check_json_file():
    """
    Will check for the json file that will act as a "database" :P.
    """
    if glob.glob("preferences.json"):
        return True
    try:
        with open("preferences.json", "w") as preferences:
            data = dict(baseDir = None)
            json.dump(data, preferences)
        logging.info("JSON file created successfully.")
        return True
    except:
        logging.error("Problem with the JSON file creation.")
        return False

def check_files():
    """
    Calls other checkers. 
    For now, will call the log dir checker and json file checker.
    """
    if not check_log_files() or not check_json_file():
        logging.critical("Problem with the file check!")
        return False
    logging.info("Files checked successfully")
    return True