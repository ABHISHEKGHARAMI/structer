# log configuration file
import logging
import os

#set up


def setup_logging():
    # Configure logging
    logging.basicConfig(filename='/home/abhishek/Documents/DataStructure&Algorithm/structer/logger/logger.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s')