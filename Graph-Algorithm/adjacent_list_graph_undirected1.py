import networkx as nx
import os
import matplotlib.pyplot as plt
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()

class UGraph:
    def __init__(self):
        self.graph = {}
        
        
    # here goes the adding the edge
    def addEdge(self,u,v):
        try:
            # for directed graph have to add two edges for the connection
            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append(v)
            
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append(u)
                
            
        except Exception:
            print(e)
            logging.info(e)
            raise Exception
        
        
    # printing the graph
    def printGraph(self):
        if not self.graph:
            print("Graph is empty.")
            logging.info("Graph is empty.")
        else:
            for vertex in self.graph:
                print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))
                logging.info(f"{vertex}  ---> {self.graph[vertex]}")
                
    def draw_graph(self,filepath):
        G = nx.Graph()
        for vertex, neighbors in self.graph.items():
            G.add_node(vertex)
            for neighbor in neighbors:
                G.add_edge(vertex, neighbor)

        nx.draw(G, with_labels=True, font_weight='bold')
        plt.title("undirected graph")
        plt.savefig(filepath)
        plt.show()
                
                
if __name__=="__main__":
    current_directory = os.getcwd()
    relative_directory = 'Graph-Algorithm/graph-images'

    full_dir = os.path.join(current_directory, relative_directory)

    if not os.path.exists(full_dir):
        os.makedirs(full_dir)

    filepath = os.path.join(full_dir, "adj_list_undirected_graph1.png")
    g1 = UGraph()
    g1.addEdge('a','b')
    g1.addEdge('a','c')
    g1.addEdge('b','f')
    g1.addEdge('c','d')
    
    g1.printGraph()
    
    g1.draw_graph(filepath)
