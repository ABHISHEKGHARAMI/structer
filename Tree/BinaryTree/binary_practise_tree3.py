# practice for binary tree
# set up the logger

import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.root = None
        
    # insert the data in the tree
    def insertTree(self,data):
        print(f"Inserting the {data} in the tree.")
        logging.info(f"Inserting the {data} in the tree.")
        if not self.root:
            self.root = TreeNode(data)
        else:
            insert_recursive(self.root,data)  
            
            
    # insert the recursive for the tree
    def insert_recursive(self,node,data):
        try:
            if node.data < data:
                if not node.right:
                    node.right = TreeNode(data)
                else:
                    self.insert_recursive(node.right,data)
            else:
                if not node.left:
                    node.left = TreeNode(data)
                else:
                    self.insert_recursive(node.left,data)
        except Exception as e:
            print(e)
            logging.error(e)
            raise Exception          
