import logging
from logging import FileHandler
from logging import Formatter
import os

LOG_PATH = 'logs'
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


def setup_logging():
    """
    Setup the logging. This method should only be called once from the
    applications main.
    """
    formatter = Formatter('%(asctime)s - %(name)s - %(thread)d - %(levelname)s - %(message)s')

    # Log on DEBUG level to the file
    filename = 'pipple_lecture.log'
    file_handler = FileHandler(os.path.join(LOG_PATH, filename))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Log on INFO level to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
