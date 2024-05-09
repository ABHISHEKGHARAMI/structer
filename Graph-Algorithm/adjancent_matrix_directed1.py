# setting up the logger file
import networkx as nx
import os
import matplotlib.pyplot as plt
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


# here we go for the directed graph using adjacent matrix approach

class Graph:
    def __init__(self,vertices_number):
        self.vertices_number = vertices_number
        self.adj_matrix = [[-1]*self.vertices_number for _ in self.vertices_number]
        self.vertices = {}
        self.vertices_list = [0] * self.vertices_number
        
        
    # setting the vertices
    def set_vertices(self,vtx,id):
        if 0<=vtx<= self.vertices_number:
            self.vertices[id] = vtx
            self.vertices_list[vtx] = id
            
            
    # setting edges
    def set_edges(self,frm,to,cost=0):
        print(f"Setting the edges from {frm} to {to}")
        logging.info(f"Setting the edges from {frm} to {to}")
        frm = self.vertices[frm]
        to = self.vertices[to]
        
        self.adj_matrix[frm][to] = cost
        
        
    # get the vertices list
    def get_verticesList(self):
        return self.vertices_list
    
    
    # get the edges
    def get_Edges(self):
        edges = []
        for i in range(self.vertices_number):
            for j in range(self.vertices_number):
                if self.adj_matrix[i][j] != -1:
                    edges.append((self.vertices[self.vertices_list[i]],self.vertices[self.vertices_list[j]],self.adj_matrix[i][j]))
        return edges
    
    
    # get matrix
    def get_Matrix(self):
        return self.adj_matrix
    

def create_graph_from_matrix(adj_matrix, vertices_list):
    G = nx.Graph()
    G.add_nodes_from(vertices_list)
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[0])):
            if adj_matrix[i][j] != -1:
                G.add_edge(
                    vertices_list[i], vertices_list[j], weight=adj_matrix[i][j])
    return G


vertices_number = int(input("enter the number of graph vertices :"))

G = Graph(vertices_number)

for i in range(vertices_number):
    print(f"{i} th vertix : ")
    id = str(input("enter the id of the vertix :"))

    G.set_vertices(i, id)
    
print(f"the vertices of the graph is : {G.verticesList}")
logging.info(f"the vertices of the graph is : {G.verticesList}")

print(f"the vertices with the proper id is : {G.vertices}")
logging.info(f"the vertices with the proper id is : {G.vertices}")


while True:
    print("1: for insert the edge setting function. 2: for exit.")
    choice = int(input("enter choice :"))
    if choice == 1:
        frm, to, cost = map(str, input(
            "enter the source , destination and cost(with comma) :").split(","))
        cost = int(cost)
        G.set_edge(frm, to, cost)

    elif choice == 2:
        break
    else:
        print("wrong choice !!")
        
print(f"the edges of the graph are : {G.get_Edges()}")
logging.info(f"the edges of the graph are : {G.get_Edges()}")

print("the adjacent matrix will be :")
logging.info("the adjacent matrix will be : ")

for i in range(G.vertices_number):
    for j in range(G.vertices_number):
        print(f"{G.adj_matrix[i][j]}", end=" ")
    print("\n")
    
logging.info(G.adj_matrix)

current_directory = os.getcwd()
relative_directory = 'Graph-Algorithm/graph-images'

full_dir = os.path.join(current_directory, relative_directory)

if not os.path.exists(full_dir):
    os.makedirs(full_dir)

# Create a NetworkX graph
G_nx = create_graph_from_matrix(G.get_Matrix(), G.get_verticesList())


# Draw the graph

plt.figure(figsize=(8, 6))
nx.draw(G_nx, with_labels=True, arrows=True, arrowstyle='->', arrowsize=15,
        node_size=1000, node_color='lightblue', font_size=12, font_weight='bold')
image_path = os.path.join(full_dir, "directed_graph.png")

plt.savefig(image_path)

# Show the graph
plt.title("Adjacent matrix directed graph.")
plt.show()
