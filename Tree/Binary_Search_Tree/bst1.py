# setting up the logger
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
        
        
    # insertion in tree
    def insertion(self,data):
        print(f"inserting {data} in the tree.")
        logging.info(f"inserting {data} in the tree.")
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.insert_recursive(self.root,data)
            
    # insertion of the tree
    def insert_recursive(self,node,data):
        try:
            if node.data < data:
                if not node.right :
                    node.right = TreeNode(data)
                else:
                    self.insert_recursive(node.right,data)
            elif node.data > data:
                if not node.left :
                    node.left = TreeNode(data)
                else:
                    self.insert_recursive(node.left,data)
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
        
        
t1 = Tree()      
while True:
    print("\n1: insert. \t 2:")
    choice = int(input("\nenter the choice :"))
    if choice == 1 :
        data = int(input("enter the data to be insert :"))
        t1.insertion(data)
        