import networkx as nx
import os
import matplotlib.pyplot as plt
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging


class Graph:
    def __init__(self):
        self.graph = {}
        
    
    #adding edge
    def addEdge(self,u,v):
        try:
            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append(v)
            
        except Exception as e:
            print(e)
            logging.info(e)
            raise e
        
    # print edges of the graph
    def printEdges(self):
        if not self.graph:
            print("graph is empty.")
            logging.info("graph is empty.")
        else:
            for vertex in self.graph:
                print(f"{vertex}  ---> {self.graph[vertex]}")
                logging.info(f"{vertex}  ---> {self.graph[vertex]}")
                
    def draw_graph(self,filepath):
        G = nx.Graph()
        for vertex, neighbors in self.graph.items():
            G.add_node(vertex)
            for neighbor in neighbors:
                G.add_edge(vertex, neighbor)
        pos = nx.spring_layout(G)  # Positions for all nodes

        nx.draw(G, pos, with_labels=True, arrows=True, font_weight='bold')
        plt.title("Graph with adjacent list representation for directed Graph :")
        plt.savefig(filepath)
        plt.show()
                
                
current_directory = os.getcwd()
relative_directory = 'Graph-Algorithm/graph-images'

full_dir = os.path.join(current_directory, relative_directory)

if not os.path.exists(full_dir):
    os.makedirs(full_dir)
    
filepath = os.path.join(full_dir, "adj_list_directed_graph1.png")
                
g2 = Graph()
g2.addEdge('a','b')
g2.addEdge('a','c')
g2.addEdge('b','e')
g2.addEdge('c','f')
g2.printEdges()

g2.draw_graph(filepath)