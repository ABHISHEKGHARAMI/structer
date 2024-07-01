# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


# detect the cycle using the dfs based style 
class Graph:
    def __init__(self,V):
        self.V = V
        self.graph = {i: [] for i in range(V)}
        
        
    # add edge for the Graph
    def addEdge(self,u,v):
        # adding the edge for the directed  graph
        self.graph[u].append(v)
        
        
    # print the graph
    def printGraph(self):
        try:
            if not self.graph:
                print("Graph is empty.")
                logging.info("Graph is empty.")
            else:
                for vertex in self.graph:
                    print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))
                    logging.info(f"{vertex}  ---> {self.graph[vertex]}")
        except Exception as e:
            print(e)
            logging.info(e)
            
            
    # module for helper function for the checking of the graph
    def cycleDetectUtil(self,v,visited,rec_stack):
        visited[v] = True
        rec_stack[v] = True
        
        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.cycleDetectUtil(neighbor,visited,rec_stack) == True:
                    return True
            elif rec_stack[neighbor] == True:
                return True
                
        # the node need to pop out for the stack
        rec_stack[v] = False
        return False
    
            

    # module for the detect cycle for the graph main function
    def cycleDetect(self):
        visited = [False] * (self.V+1)
        rec_stack = [False] * (self.V+1)
        for node in range(self.V):
            if visited[node] == False:
                if self.cycleDetectUtil(node,visited,rec_stack) == True:
                    return True
        return False
    
    

# main function
g1 = Graph(4)
g1.addEdge(0,1)
g1.addEdge(1,2)
g1.addEdge(2,3)
g1.addEdge(3,0)

if g1.cycleDetect() == 1:
    print("the graph contains the cycle.")
    logging.info("the graph contains the cycle.")
else:
    print("the graph does not contains cycle.")
    logging.info("the graph does not contain cycle.")
            
        
    