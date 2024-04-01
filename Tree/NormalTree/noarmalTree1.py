# building the basic tree data structure (not binary tree) for normal tree
# and generate the real picture of the tree

# *** setting up the logger file
import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append("D:/geeks1.0/structer")
import logging
from settings import setup_logging

# here goes the tree
# importing the modules for that


class Treenodes:
    def __init__(self,value):
        self.value = value
        self.children = []
        
        
class Tree:
    def __init__(self):
        self.root = None
    
    # for finding the node
    def _find_node(self,node,value):
        if node.value == value:
            return node
        for child in node.children:
            found = self._find_node(child,value)
            if found:
                return found
        return None
    
    # find the parent and children
    def _find_parent_child(self,node,value):
        for child in node.children:
            if child.value == value:
                return node,child
            parent, node_to_delete = self._find_parent_child(child,value)
            if node_to_delete:
                return parent, node_to_delete
            return None,None
    
    # for inserting the data in the tree
    def insertData(self,parent_data,data):
        if not self.root:
            self.root = Treenodes(data)
        parent_node = self._find_node(self.root,parent_data)
        if parent_node:
            parent_node.children.append(data)
            return True
        return None
    
    
    # delete the node for the tree
    def deleteNode(self,data):
        if not self.root:
            return False
        if self.root.data == data:
            self.root = None
            return True
        parent_node , node_to_delete = self._find_parent_child(self.root,value)
        if parent_node and node_to_delete:
            parent_node.children.remove(node_to_delete)
            return True
        return False
    
    # function for networks
    def to_networkx(self):
        G = nx.Graph()
        self.add_Edges(self.root,G)
        return G
    
    
    # def add edges
    def add_Edges(self, node , G):
        for child in node.children:
            G.add_edge(node.data, child.data)
            self.add_Edges(child,G)
        
        
    # Executing the main function
    
tree = Tree()
tree.insertData(None,1)
tree.insertData(1,2)
tree.insertData(1,3)
tree.insertData(2,4)
tree.insertData(2,5)

G = tree.to_networkx()

# time to plot the tree
plt.figure(figsize = (8,6))
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=5000, node_color="skyblue", font_size=20, font_weight="bold", arrowsize=20)
plt.title("Tree Visualization")
plt.show()
        