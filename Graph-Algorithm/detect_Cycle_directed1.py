# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


# detect the cycle using the dfs based style 
class Graph:
    def __init__(self,V):
        self.graph = {}
        self.vertices = V
        
    # add edge for the Graph
    def addEdge(self,u,v):
        # adding the edge for the directed  graph
        if u not in self.graph:
            self.graph[u] = []
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
            
            
    # module for the check cycle for the graph
    def isCycle(self):
        visited = [False]*self.vertices
        rec_stack = [False]*self.vertices
        
        for node in range(self.vertices):
            if not visited[node]:
                if self.isCycleUtil(node,visited,rec_stack):
                    return False
                return True
            
            
    # helper module for the check the each node with the neighbors 
    def isCycleUtil(self,v,visited,rec_stack):
        visited[v] = True
        rec_stack[v] = True
        
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.isCycleUtil(neighbor,visited,rec_stack):
                    return True
                elif rec_stack[neighbor] :
                    return True
            
        # if this won't the case then the case will be
        rec_stack[v] = False
        return False
    
    
    
v = int(input("enter the vertices for the graph :"))

g1 = Graph(v)


while True:
    print("1: for add edge.\t 2: Check the Cycle.\t 3: Print Graph.")
    print("0: for exit")
    choice = int(input("enter the choice :"))
    if choice == 0:
        exit(0)
    elif choice == 1:
        u ,v = map(int,input("enter the to vertices :").split(","))
        g1.addEdge(u,v)
    elif choice == 2:
        if g1.isCycle():
            print("Graph contains the cycle.")
            logging.info("Graph contains the cycle.")
        else:
            print("Graph does not contains the cycle.")
            logging.info("Graph does not contains the cycle.")
    elif choice == 3:
        print("Printing the graph.")
        logging.info("Printing the graph.")
        g1.printGraph()
        
    else:
        print("Wrong choice mate!!")
        logging.info("Wrong choice mate!!")
        
        print("Here we go again !!")
                
        
            


        
    