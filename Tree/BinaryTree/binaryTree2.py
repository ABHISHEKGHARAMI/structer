# importing the networkx and matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import os

# setting up the python logger for update
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


# class for treenode
class TreeNode:
    def __init__(self,data):
        self.data = data    
        self.left = None
        self.right = None
        
        
# tree class
class Tree:
    def __init__(self):
        self.root = None
        
    