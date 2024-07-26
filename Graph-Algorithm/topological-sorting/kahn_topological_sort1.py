# kahn algorithm for the topological sort

# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


# queue class
class Queue:
    def __init__(self):
        self.queue = []
        
    # enQueue op
    def enQueue(self,data):
        self.queue.append(data)
    # checking the queue is empty or not
    def isEmpty(self):
        return len(self.queue) == 0
    #dequeue op
    def deQueue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        
    # len of the queue
    def __len__(self):
        return len(self.queue)
    
# Graph structure
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = { vertex : [] for vertex in self.vertices}
        
    # adding edge of the graph
    def addEdge(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
            logging.info(f"vertex : {u} added to the vertex  : {v}")
        else:
            self.graph[u] = [v]
            logging.info(f"vertex : {u} added to the vertex  : {v}")
    
    
    # printing the graph for the conformation
    def printGraph(self):
        print("printing the graph :")
        logging.info("printing the graph :")
        for vertex in self.graph:
            print(f"{vertex}:{'->'.join(self.graph[vertex])}")
            logging.info(f"{vertex} : {self.graph[vertex]}")
            
            
    # kahn algorithm for the topological sort
    def topoSortKahn(self):
        try:
            # intialize the vertices the of in-degree 0
            in_degree = { v: 0 for v in self.vertices}
            
            # calculate the all the in-degree of the graph vertices
            for u in self.graph:
                for v in self.graph[u]:
                    in_degree[v] += 1
            
            # enQueue all the vertices that has in-degree 0
            Q1 = Queue()
            for v in self.graph:
                if in_degree[v] == 0:
                    Q1.enQueue(v)
                    
            top_order = []
            
            # process the Queue for the sorting the graph
            while not Q1.isEmpty():
                u = Q1.deQueue()
                top_order.append(u)
                
                # now time to process the queue all the outgoing edge 
                for v in self.graph[u]:
                    in_degree[v] = in_degree[v] - 1
                    if in_degree[v] == 0:
                        Q1.enQueue(v)
                        
            # now check the topological sort is even possible or not for the graph
            if len(top_order) == len(self.vertices):
                result = '->'.join(top_order)
                print("topological sort is possible for the graph,no cycle found.")
                logging.info("topological sort is possible for the graph,no cycle found.")
                print(f"the topological sort of the graph is : {result}")
                logging.info(f"the topological sort of the graph is : {result}")
            else:
                print("topological sort is not possible, cycle found.")
                logging.info("topological sort is not possible, cycle found.")
            
        except Exception as e:
            print(e)
            logging.info(e)
            raise e
            

vertices = ['a', 'b', 'c', 'd', 'e', 'f']


g1 = Graph(vertices)

g1.addEdge('a', 'c')
g1.addEdge('b', 'c')
g1.addEdge('b', 'd')
g1.addEdge('c', 'e')
g1.addEdge('d', 'f')
g1.addEdge('e', 'f')

g1.printGraph()

g1.topoSortKahn()

