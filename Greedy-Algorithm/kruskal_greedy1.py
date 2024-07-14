# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
    # find for the root
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # union for the root
    def Union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
                
# graph structure
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.v = len(self.vertices)
        self.index_map = { vertex : idx for idx,vertex in enumerate(self.vertices)}
        self.edges = []
        
    # add edges for the graph
    def addEdge(self,u,v,w):
        if u in self.vertices and v in self.vertices:
            self.edges.append((w,u,v))
        else:
            print(f"{u} or {v} or both not added in the vertex list.")
            logging.info(f"{u} or {v} or both not added in the vertex list.")
            
    # print the graph
    def printGraph(self):
        try:
            if not self.edges:
                print("Graph is empty.")
                logging.info("Graph is empty.")
            else:
                print("Printing the graph.")
                logging.info("Printing the graph.")
                for edge in self.edges:
                    print(f"{edge[1]} - {edge[2]}: {edge[0]}")
                logging.info("Graph printed successfully.")
        except Exception as e:
            print(e)
            logging.info(e)
            raise e
        
    
    
    # kruskal algorithm for the MST
    def krushkalGreedyMST(self):
        self.edges.sort()
        
        dsu = DSU(self.v)
        mst_edges = []
        total_weight = 0
        
        for edge in self.edges:
            weight , u ,v = edge
            
            u_idx = self.index_map[u]
            v_idx = self.index_map[v]
            
            if dsu.find(u_idx) != dsu.find(v_idx):
                dsu.Union(u_idx,v_idx)
                mst_edges.append((u,v,weight))
                total_weight += weight
                
        print("Edges in MST:")
        for u, v, weight in mst_edges:
            print(f"{u} - {v}: {weight}")
            logging.info(f"{u} - {v}: {weight}")
        print(f"Total weight of MST: {total_weight}")
        logging.info(f"Edges in MST: {mst_edges}")
        logging.info(f"Total weight of MST: {total_weight}")
        
        
vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

g1 = Graph(vertices)

# Adding 14 edges
g1.addEdge('a', 'b', 4)
g1.addEdge('a', 'c', 2)
g1.addEdge('b', 'c', 5)
g1.addEdge('b', 'd', 10)
g1.addEdge('c', 'e', 3)
g1.addEdge('d', 'f', 11)
g1.addEdge('e', 'd', 4)
g1.addEdge('e', 'f', 8)
g1.addEdge('e', 'g', 7)
g1.addEdge('f', 'h', 1)
g1.addEdge('g', 'h', 2)
g1.addEdge('h', 'i', 6)
g1.addEdge('i', 'j', 4)
g1.addEdge('j', 'a', 5)


# printing the graph
g1.printGraph()


# kruskal algo
g1.krushkalGreedyMST()
