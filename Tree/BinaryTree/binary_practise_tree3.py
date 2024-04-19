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
        
        
    # find the height
    def height(self,node):
        try:
            if not node:
                return 0
            else:
                lheight = self.height(node.left)
                rheight = self.height(node.right)
                return max(lheight,rheight) + 1
        except Exception as e:
            print(e)
            logging.error(e)
            raise Exception 
        
    # find the min value for the tree
    def find_min(self,node):
        if not node:
            return
        else:
            while node.left:
                node = node.left
            return node.data
        
    
    # delete the node for the tree
    def deleteNode(self,data):
        print(f"Delete {data} from the tree.")
        logging.info(f"Delete {data} from the tree.")
        self.deleteNode_recursive(self.root,data)
        
        
    # delete recursive for the tree
    def deleteNode_recursive(self,node,data):
        try:
            if not node or not data:
                return node
            else:
                if node.data < data:
                    node.right = self.deleteNode_recursive(node.right,data)
                elif node.data > data:
                    node.left = self.deleteNode_recursive(node.left,data)
                else:
                    if not node.left:
                        return node.right
                    elif not node.right:
                        return node.left
                    else:
                        temp_node = self.find_min(node.right)
                        node.data = temp_node.data
                        node.right = self.deleteNode_recursive(node.right,temp_node.data)
                return node
                        
        except Exception as e:
            print(e)
            logging.error(e)
            raise Exception
        
    # search for the tree
    def searchTree(self,node,data):
        if not node:
            return False
        else:
            if node.data == data:
                return  True
            elif node.data < data:
                return self.searchTree(node.right,data)
            else:
                return self.searchTree(node.left,data)
            
            
    #Traversal for the tree
    def preorder_traversal(self):
        if self.root:
            self.preorder_recur(self.root)
            
    # recursive
    def preorder_recur(self,node):
        if not node:
            self.preorder_recur(node.left)
            print(f"->{node.data}")
            logging.info(f"->{node.data}")
            self.preorder_recur(node.right)
    
    # traversal for the post order      
            
        
        
        
root_data = int(input("enter the root for the data :"))
list1 = list(map(int,input("enter the all the tree data for the list (with comma):").split(",")))
t1 = Tree()
t1.insertTree(root_data)
for i in list1:
    t1.insertTree(i)

while True:
    print("\n1: insert \n2: delete \n3: search \n 0: exit")
    print("\n4: inorder traversal .")
    choice = int(input("enter the choice :"))
    if choice == 0:
        exit(0)
    elif choice == 1:
        data = int(input("enter the data to the insert in the tree :"))
        t1.insertTree(data)
    elif choice == 2:
        data = int(input("enter the data to be delete :"))
        t1.deleteNode(data)
    elif choice == 3:
        data = int(input("enter the data to search :"))
        if t1.searchTree(t1.root,data) == False:
            print(f"{data} is not present in the tree.")
            logging.info(f"{data} is not present in the tree.")
        else:
            print(f"{data} is  present in the tree.")
            logging.info(f"{data} is present in the tree.")
            
    elif choice == 4:
        t1.preorder_traversal()
        
