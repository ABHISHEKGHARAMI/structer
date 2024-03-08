# log configuration file
import logging
import os

#set up


def setup_logging():
    # Configure logging
    logging.basicConfig(filename='D:/python_exercise_geeks/structer-1/logger/logger.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s')