# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


# here i go for the code for the undirected graph for the adjacency matrix representation

class Graph:
    def __init__(self,verticesNum):
        self.verticesNum = verticesNum
        self.adjacent_Matrix = [[-1]*self.verticesNum for _ in range(self.verticesNum)]
        self.vertices = {}
        self.verticesList = [0] * self.verticesNum
        
        
    # setting the vertices
    def set_vertices(self,vtx,id):
        if 0<=vtx<=self.verticesNum:
            self.vertices[id] = vtx
            self.verticesList[vtx] = id
            
            
    # setting edge
    def set_edge(self,frm,to,cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        
        self.adjacent_Matrix[frm][to] = cost
        
        self.adjacent_Matrix[to][frm] = cost
        
    
    # get the full vertices list
    def get_verticesList(self):
        return self.verticesList
    
    
    #get edges
    def get_Edges(self):
        edges = []
        for i in range(self.verticesNum):
            for j in range(self.verticesNum):
                edges.append((self.vertices[i],self.vertices(j),self.adjacent_Matrix[i][j]))
                
        return edges
    
    
    # get matrix
    def get_Matrix(self):
        return self.adjacent_Matrix
    
    
# main execution of the program
vertices_number = int(input("enter the number of graph vertices :"))

G = Graph(vertices_number)

for i in range(vertices_number):
    print(f"{i} th vertix : ")
    id  = str(input("enter the id of the vertix :"))
    
    G.set_vertices(i,id)
    
print(f"the vertices of the graph is : {G.verticesList}")
logging.info(f"the vertices of the graph is : {G.verticesList}")

print(f"the vertices with the proper id is : {G.vertices}")
logging.info(f"the vertices with the proper id is : {G.vertices}")