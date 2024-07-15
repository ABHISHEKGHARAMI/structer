# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()

# graph class for the topological sort
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = { vertex : [] for vertex in self.vertices}
        
    # add edge for the u and v
    def addEdge(self,u,v):
        if u in self.vertices:
            self.graph[u].append(v)
        else:
            print(f"{u} is not found in the vertices")
            logging.info(f"{u} is not found in the vertices")
            
    # topological sort for the graph
    def topologicalSort(self):
        visited = { v : False for v in self.vertices}
        stack = []
        
        for vertex in self.vertices:
            if not visited[vertex]:
                self.topologicalSortUtill(vertex,visited,stack)
                
        # print the stack
        print("The topological sort for the graph is :")
        logging.info("The topological sort for the graph is :")
        print("->".join(stack))
        logging.info("->".join(stack))
        
        
    # topological sort helper union function
    def topologicalSortUtill(self,v,visited,stack):
        visited[v] = True
        
        # recurr all the neighbors for the node
        for i in self.graph[v]:
            if  not visited[i]:
               self.topologicalSortUtill(i,visited,stack) 
               
        stack.insert(0,v)
        

vertices = ['a', 'b', 'c', 'd', 'e', 'f']
g = Graph(vertices)
g.addEdge('a', 'c')
g.addEdge('b', 'c')
g.addEdge('b', 'd')
g.addEdge('c', 'e')
g.addEdge('d', 'f')
g.addEdge('e', 'f')


g.topologicalSort()