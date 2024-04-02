# building up the tree data structure 

# setting up the logger file
import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

# setting up the tree data structure


class Treenode:
    def __init__(self, value):
        self.value = value
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

    def _find_node(self, node, value):
        if node.value == value:
            return node
        for child in node.children:
            found = self._find_node(child, value)
            if found:
                return found
        return None

    def _find_parent_child(self, node, value):
        for child in node.children:
            if child.value == value:
                return node, child
            parent, node_to_delete = self._find_parent_child(child, value)
            if node_to_delete:
                return parent, node_to_delete
        return None, None

    def insert_data(self, parent_value, value):
        if not self.root:
            self.root = Treenode(value)
            return True
        parent_node = self._find_node(self.root, parent_value)
        if parent_node:
            new_node = Treenode(value)
            parent_node.children.append(new_node)
            return True
        return False

    def delete_node(self, value):
        if not self.root:
            return False
        if self.root.value == value:
            self.root = None
            return True
        parent_node, node_to_delete = self._find_parent_child(self.root, value)
        if parent_node and node_to_delete:
            parent_node.children.remove(node_to_delete)
            return True
        return False

    def to_networkx(self):
        G = nx.Graph()
        self._add_edges(self.root, G)
        return G

    def _add_edges(self, node, G):
        for child in node.children:
            G.add_edge(node.value, child.value)
            self._add_edges(child, G)


# Executing the main function
tree = Tree()
tree.insert_data(None, 1)
tree.insert_data(1, 2)
tree.insert_data(1, 3)
tree.insert_data(2, 4)
tree.insert_data(2, 5)

G = tree.to_networkx()

# Plotting the tree
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=5000, node_color="skyblue",
        font_size=20, font_weight="bold", arrowsize=20)
plt.title("Tree Visualization")
plt.savefig('pic.png')
plt.show()
