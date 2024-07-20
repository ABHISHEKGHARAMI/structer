# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()

# problem statement - kahn algorithm for the topological sort
class Queue:
    def __init__(self):
        self.queue = []
        
    # enqueue the data
    def enQueue(self,data):
        self.queue.append(data)
        
    # check the queue is empty
    def is_Empty(self):
        return len(self.queue) == 0
    
    # dequeue the tree
    def deQueue(self):
        if self.is_Empty()  != True:
            return self.queue.pop(0)
        
    # return the length of the Queue
    def __len__(self):
        return len(self.queue)
    
    
# here goes the topological sort for the directed acyclic graph
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = {vertex : [] for vertex in self.vertices}
        
    # add Edge for the graph
    def addEdge(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
            
    # function for the topological sort
    def kahn_topoSort(self):
        try:
            in_degree = { v : 0 for v in self.vertices }
            for u in self.graph:
                for v in self.graph[u]:
                    in_degree[v] += 1       
            
            # enQueue the nodes which has in_degree is zero
            q1 = Queue()
            for v in self.graph:
                if in_degree[v] == 0:
                    q1.enQueue(v)
                    
                    
            top_order = [] # top order for storing the queue
            
            # process the queue
            while not q1.is_Empty():
                u = q1.deQueue()
                top_order.append(u)
                
                # decrease the in_degree for if it is in the graph
                for v in self.graph[u]:
                    in_degree[v] = in_degree[v] - 1
                    # if the in degree is zero  then enqueue that node in queue
                    if in_degree[v] == 0:
                        q1.enQueue(v)
            
            # here goes the checking part for the queue
            if len(top_order) == self.vertices:
                print("the topological sort of the graph is :")
                logging.info("the topological sort of the graph is : ")
                print('->'.join(top_order))
                logging.info('->'.join(top_order))
            else:
                print("there exist a cycle in the graph so that topological sort of the graph is not possible.")
                logging.info("there exist a cycle in the graph so that topological sort of the graph is not possible")
                
                               
        except Exception as e:
            print(e)
            logging.info(e)
            raise e
        
vertices = ['a','b','c','d','e','f']

g = Graph(vertices)


g.addEdge('a', 'c')
g.addEdge('b', 'c')
g.addEdge('b', 'd')
g.addEdge('c', 'e')
g.addEdge('d', 'f')
g.addEdge('e', 'f')

# topological sort of the graph

g.kahn_topoSort()

