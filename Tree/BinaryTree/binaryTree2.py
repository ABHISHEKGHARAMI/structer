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
    
    # delete node
    def deleteNode(self,data):
        print(f"Deleting the {data} form the tree .")
        logging.info(f"Deleting the {data} form the tree .")
        self.deleteNode_recursive(self.root,data)
        
        
    # adding the recursive delete function
    def deleteNode_recursive(self,node,data):
        if not node:
            return
        if node.data < data:
            node.left = self.deleteNode_recursive(node.left,data)
        elif node.data > data:
            node.right = self.deleteNode_recursive(node.right,data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self.findMin(node)
                node.data = min_node.data
                node.right = self.deleteNode_recursive(node.right,min_node.data)
                
                
    # print the inorder,postorder and preorder traversal
    def inorder_trav(self):
        print("Doing inorder traversal")
        logging.info("Doing inorder traversal")
        self.inorder_utill_recursive(self.root)
    
    # recursive
    def inorder_utill_recursive(self,node):
        if node:
            self.inorder_utill_recursive(node.left)
            print(f"-->{node.data}",end=" ")
            logging.info(f"{node.data}-->")
            self.inorder_utill_recursive(node.right)
    #postorder traversal

    def postorder_trav(self):
        print("Doing Postorder traversal")
        logging.info("Doing Postorder traversal")
        self.postorder_utill_recursive(self.root)
    
    # recursive
    def postorder_utill_recursive(self, node):
        if node:
            self.postorder_utill_recursive(node.left)
            self.postorder_utill_recursive(node.right)
            print(f"-->{node.data}", end=" ")
            logging.info(f"{node.data}-->")
            
    def preorder_trav(self):
        print("Doing Preorder traversal")
        logging.info("Doing Preorder traversal")
        self.preorder_utill_recursive(self.root)
        
    def preorder_utill_recursive(self, node):
        if node:
            print(f"-->{node.data}", end=" ")
            logging.info(f"{node.data}-->")
            self.preorder_utill_recursive(node.left)
            self.preorder_utill_recursive(node.right)
        
    
    
# checking the execution
tree = Tree()

arr = [23,24,45,35]

for i in arr:
    tree.insertNode(i)

tree.inorder_trav()