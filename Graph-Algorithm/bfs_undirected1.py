# setting up the logger
import networkx as nx
import os
import matplotlib.pyplot as plt
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


class Queue:
    def __init__(self):
        self.queue = []
        
    def push(self,data):
        if data:
            print(f"{data} inserting in the queue.")
            logging.info(f"{data} inserting in the queue.")
            self.queue.append(data)
            
    # pop operation
    def pop(self):
        if self.isEmpty() != 1:
            return self.queue.pop(0)
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0