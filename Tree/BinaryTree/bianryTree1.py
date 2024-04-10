# implementation of the binary tree
#importing the module
import matplotlib.pyplot as plt
import networkx as nx
import os
# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()

# building the tree node
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
# building the tree class
class Tree:
    def __init__(self):
        self.root = None
        
    # inserting the value for the tree
    def insertNode(self,data):
        try:
            if not self.root:
                self.root = TreeNode(data)
            else:
                self.insertNode_Recursive(self.root,data)
        except Exception as e:
            print(e)
            logging.error(e)
            
            
    # recursive function for the value for the data
    def insertNode_Recursive(self,node,value):
        try:
            if node.value > value :
                if node.left :
                    self.insertNode_Recursive(node.left,value)
                else:
                    node.left = TreeNode(value)
            elif node.value < value:
                if node.right :
                    self.insertNode_Recursive(node.right,value)
                else:
                    node.right = TreeNode(value)
        except Exception as e:
            print(e)
            logging.error(e)
            
            
    # inorder traversal
    def inOrder_Traversal(self):
        print("Doing inorder traversal .....")
        logging.info("Doing inorder traversal ....")
        self.inOrder_Traversal_recursive(self.root)
    
    # recursive inorder traversal  
    def inOrder_Traversal_recursive(self,node):
        if node:
            self.inOrder_Traversal_recursive(node.left)
            print(f"->{node.value}")
            logging.info(f"->{node.value}")
            self.inOrder_Traversal_recursive(node.right)
    
    
    # recursive postorder travesal
    def postOrder_Traversal(self):
        logging.info(f"Post order traversal")
        self.postOrder_traversal_recursive(self.root)
        
    # recursive function for the postorder
    def postOrder_traversal_recursive(self,node):
        if node:
            self.postOrder_traversal_recursive(node.left)
            self.postOrder_traversal_recursive(node.right)
            print(f"->{node.value}")
            logging.info(f"->{node.value}")      
            
    # pre Order traversal for the tree
    def preOrder_Traversal(self):
        logging.info("PreOrder Traversal ....")
        self.preOrder_recursive_traversal(self.root)
        
    # pre order recursive algorithm
    def preOrder_recursive_traversal(self,node):
        if node:
            print(f"->{node.value}",end=" ")
            logging.info(f"->{node.value}")
            self.preOrder_recursive_traversal(node.left)
            self.preOrder_recursive_traversal(node.right)
            
    # find the height of the tree recursively
    def find_height(self):
        try:
            return self.height_recursive(self.root)
        except Exception as e:
            print(e)
            logging.info(e)  
            
    # recursive function
    def height_recursive(self,node):
        if not node:
            return 0
        else:
            return max(self.height_recursive(node.left),self.height_recursive(node.right))+1
    # find the min node
    def _find_min(self,node):
        while node.left:
            node = node.left
        return node
    
    # print the tree data from the k th node
    def print_from_kth_distance(self,k):
        return self.print_recursive_kth(self.root,k)
    
    # recursive function for this
    def print_recursive_kth(self,node,k):
        if not node or k< 0:
            return
        if node or k == 0:
            print(f"{node.value}", end=" ")
            logging.info(f"{node.value}")
        else:
            self.print_recursive_kth(node.left)
            self.print_recursive_kth(node.right)
    
    # delete node
    def deleteNode(self,value):
        print(f"Deleting the value {value} from the tree ...")
        logging.info(f"Deleting the value {value} from the tree ...")
        self.deleteNode_recursive(self.root,value)
        
    
    #delete node recursively
    def deleteNode_recursive(self,node,value):
        try:
            if not node:
                return node
            if node.value > value:
                node.left = self.deleteNode_recursive(node.left,value)
            elif node.value < value:
                node.right = self.deleteNode_recursive(node.right,value)
            else:
                # node has  children
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                # node has 2 children
                min_node = self._find_min(node.right)
                # copy the value to the node value
                node.value = min_node.value
                # delete the min value
                node.right = self.deleteNode_recursive(node.right,min_node.value)
        except Exception as e:
            print(e)
            logging.error(e)
            
    
    # adding the networkx for the graph plotting
    def to_networkx(self):
        try:
            G = nx.Graph()
            if self.root:
                self._add_edges(self.root,G)
            return G
        except Exception as e:
            print(e)
            logging.error(e)
            
            
    # adding the edges of the tree nodes
    def _add_edges(self,node,G):
        if node.left:
            G.add_edge(node.value,node.left.value)
            logging.info(f"Adding edge between {node.value} and {node.left}")
            self._add_edges(node.left,G)
        if node.right:
            G.add_edge(node.value,node.right.value)
            self._add_edges(node.right,G)
            logging.info(f"Adding edge between {node.value} and {node.right}")
            
    
    # visualize and save the image
    def visualize_saveImage(self,file_path):
        G = self.to_networkx()
        plt.figure(figsize=(8,6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=5000, node_color="skyblue",
                font_size=20, font_weight="bold", arrowsize=20)
        plt.title("Binary Tree Visualization")

        # Save the plot to the specified directory
        plt.savefig(file_path)
        plt.show()
          # Close the plot to free resources

#executing the main function .
tree = Tree()
tree.insertNode(5)
tree.insertNode(3)
tree.insertNode(7)
tree.insertNode(2)
tree.insertNode(4)
tree.insertNode(6)
tree.insertNode(8)


# printing the height of the tree
print(f"The height of the binary tree is : {tree.find_height()}")
logging.info(f"The height of the binary tree is : {tree.find_height()}")
#exe
k = int(input(f"enter the tree of height {tree.find_height()} :"))

tree.print_from_kth_distance(k)
logging.info(f"{tree.print_from_kth_distance(k)}")
tree.inOrder_Traversal()

# adding the pre order and post order traversal of the tree
tree.preOrder_Traversal()

tree.postOrder_Traversal()

current_directory = os.getcwd()
relative_directory = 'Tree/tree_image'

full_dir = os.path.join(current_directory,relative_directory)

if not os.path.exists(full_dir):
    os.makedirs(full_dir)
file_path = os.path.join(full_dir,'binary_tree1.png')

tree.visualize_saveImage(file_path=file_path)

tree.deleteNode(4)

tree.to_networkx()

delete_path = os.path.join(full_dir,'binary_tree_delete1.png')

tree.visualize_saveImage(file_path=delete_path)