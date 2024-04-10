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
        
    def insertNode(self,data):
        print(f"Inserting {data} in the tree .")
        logging.info(f"Inserting {data} in the tree .")
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.insert_recursive(self.root,data)
    
    # recursive function for the insertion
    def insert_recursive(self,node,data):
        try:
            if node.data < data :
                if node.left:
                    self.insert_recursive(node.left,data)
                else:
                    node.left = TreeNode(data)
            else:
                if node.right :
                    self.insert_recursive(node.right,data)
                else:
                    node.right = TreeNode(data)
        except Exception as e:
            print(e)
            logging.info(e)
            raise EOFError
        
    # return the height
    def heightTree(self,node):
        if not node:
            return 0
        else:
            return max(self.heightTree(node.left),self.heightTree(node.right)) + 1
        
    # find the min value
    def findMin(self,node):
        while node.left:
            node = node.left
        return node