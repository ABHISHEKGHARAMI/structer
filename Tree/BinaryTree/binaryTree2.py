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

# queue class for the level order traversal
class Queue:
    def __init__(self):
        self.queue = []
        
    # push
    def push(self,node):
        #print(f"{node.data} pushed in the queue.")
        #logging.info(f"{node.data} pushed in the queue.")
        self.queue.append(node)
        
    # pop 
    def pop(self):
        if self.emptyQueue() == True:
            print("Queue is empty .")
        else:
            return self.queue.pop(0)
    
    # check empty
    def emptyQueue(self):
        if len(self.queue) == 0:
            return True
        else:
            return False


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
            
    # level order traversal
    def levelorder_traversal(self):
        try:
            print("\nlevel order traversal.")
            logging.info("level order traversal.")
            q1 = Queue()
            if not self.root:
                return
            q1.push(self.root)
            while q1.emptyQueue() == False:
                node_queue = q1.queue[0]
                print(f"-->{node_queue.data}",end=" ")
                logging.info(f"==>{node_queue.data}")
                q1.pop()
                if node_queue.left:
                    q1.push(node_queue.left)
                if node_queue.right:
                    q1.push(node_queue.right)
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
        
        
        
    # size of the tree
    def sizetree(self,node):
        try:
            if not node:
                return 0
            else:
                return self.sizetree(node.left) + 1 + self.sizetree(node.right)
        except Exception as e:
            print(e)
            logging.error(e)
            raise Exception
        
    
    # find the maximum of the tree
    def maxElement(self,node):
        min = -1111
        if not node:
            return min
        else:
            res = node.data
            lmax = self.maxElement(node.left)
            rmax = self.maxElement(node.right)
            res = max(res,max(lmax,rmax))
            return res
            
    
    
# checking the execution
tree = Tree()

arr = [23,24,45,35]

for i in arr:
    tree.insertNode(i)

tree.inorder_trav()

tree.levelorder_traversal()

print(f"The size of the binary tree is : {tree.sizetree(tree.root)}")
logging.info(f"The size of the binary tree is : {tree.sizetree(tree.root)}")

# max element
print(f"the max value of the tree is : {tree.maxElement(tree.root)}")
logging.info(f"the max value of the tree is : {tree.maxElement(tree.root)}")
