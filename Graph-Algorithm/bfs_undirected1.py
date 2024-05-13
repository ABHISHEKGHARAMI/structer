# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


class Queue:
    def __init__(self):
        self.queue = []
        
    def push(self,data):
        if data:
            print(f"{data} inserting in the queue.")
            logging.info(f"{data} inserting in the queue.")
            self.queue.append(data)
            
    # pop operation
    def pop(self):
        print(f"poping the value : {self.queue[0]}")
        logging.info(f"poping the value : {self.queue[0]}")
        if self.isEmpty() != 1:
            return self.queue.pop(0)
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
        
        
# Graph class for the Undirected graph
class UGraph:
    def __init__(self):
        self.graph = {}
        
    # add edge for the graph
    def addEdge(self,u,v):
        try:
            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append(v)
            
            
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append(u)
        except Exception as e:
            print(e)
            logging.info(e)
            raise e
        
        
    # getting the vertex of the graph
    def getVertex(self):
        if not self.graph:
            return []
        a = list(self.graph.keys())
        return a
        
    # bfs for the graph
    def bfs(self,start):
        try:
            visited = set()
            q1 = Queue()
            q1.push(start)
            while q1.isEmpty() != 1:
                vertex = q1.pop()
                if vertex not in visited:
                    print(f"--->{vertex}",end=" ")
                    logging.info(f"--->{vertex}")
                    visited.add(vertex)
                    for neighbors in self.graph[vertex]:
                        if neighbors not in visited:
                            q1.push(neighbors)
        except Exception as e:
            print(e)
            logging.info(e)
            raise e
        
        
# main Execution of the program
g1 = UGraph()
g1.addEdge('a','b')
g1.addEdge('a','c')
g1.addEdge('b','e')
g1.addEdge('c','f')

keys = g1.getVertex()

print(f"the vertex of the graphs are :")
logging.info("the vertex of the graphs are :")
for i in keys:
    print(i,end=" ")
logging.info(f"keys : {keys}")

start = str(input("choose any key and enter the key for the bfs to start :"))

g1.bfs(start)


            