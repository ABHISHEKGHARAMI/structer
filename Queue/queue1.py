# setting up the logger

import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

# setting the Queue for the class
class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = len(self.queue) - 1
        
    # enQueue for the data
    def enQueueQueue(self,data):
        try:
            pass
        except Exception as e:
            print(e)
            logging.error(e)
            
    # deQueue for the data
    def deQueue(self):
        try:
            pass
        except Exception as e:
            print(e)
            logging.error(e)
            
    # print the Queue
    def printQueue(self):
        try:
            pass
        except Exception as e:
            print(e)
            logging.error(e)
            
    