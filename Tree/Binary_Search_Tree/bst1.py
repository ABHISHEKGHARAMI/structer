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
        
    # height of the tree
    def height(self,node):
        try:
            if node == None:
                return 0
            else:
                lheight = self.height(node.left)
                rheight = self.height(node.right)
                return max(lheight,rheight) + 1
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
        
        
        
    # find the min of the tree
    def find_min(self,node):
        try:
            if not node:
                return
            else:
                while node.left:
                    node = node.left
                return node.data
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
        
        
    # delete the node
    def delete(self,data):
        print(f"deleting the {data} from the tree.")
        logging.info(f"deleting the {data} from the tree.")
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
            logging.info(e)
            raise Exception
        
        
t1 = Tree()      
while True:
    print("\n1: insert. \t 2: height. \t 3: find min. \t 4: delete.")
    choice = int(input("\nenter the choice :"))
    if choice == 1 :
        data = int(input("enter the data to be insert :"))
        t1.insertion(data)
        
    elif choice == 2:
        h1 = t1.height(t1.root)
        print(f"the height of the tree is : {h1}")
        logging.info(f"the height of the tree is : {h1}")
        
        
    elif choice == 3:
        print(f"the min element of the tree is : {t1.find_min(t1.root)}")
        logging.info(f"the min element of the tree is : {t1.find_min(t1.root)}")
        
        
    elif choice == 4:
        data = int(input("enter the data for delete :"))
        t1.delete(data)
        