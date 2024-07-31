# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()



# class for the graph
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = { vertex : [] for vertex in self.vertices }
        
    # adding th edge
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    # print the graph
    def printGraph(self):
        for vertex in self.vertices:
            print(f"{vertex}:{'->'.join(self.graph[vertex])}")
            logging.info(f"{vertex}:{'->'.join(self.graph[vertex])}")
    # dfs helper function
    def dfsUtil(self,v,visited):
        visited[v] = True
        
        for neighbor in self.graph[v]:
            # check if it is not visited
            if not visited[neighbor]:
                self.dfsUtil(neighbor,visited)
                
    # check the graph is connected or not
    def isConnected(self):
        visited = { vertex : False for vertex in self.vertices }
        
        # if any vertex has 0 edge then break the cycle not connected vertex
        for i in self.vertices:
            if len(self.graph[i]) !=0:
                break
            
        if i == len(self.vertices):
            return True
        
        # check the dfs traversal
        self.dfsUtil(i,visited)
        
        for i in self.vertices:
            if visited[i]  == False and len(self.graph[i])>0:
                return False
        return True
    
    # check for the euclerian path for graph
    def euclerainPath(self):
        if self.isConnected() == False:
            return 0
        else:
            odd = 0
            for i in self.vertices:
                if len(self.graph[i])%2 != 0 :
                    odd += 1
            if odd == 0:
                return 2
            elif odd== 2:
                return 1
            else:
                return 0
            
    # checking and printing the euclerian path or cycle based on the result came
    def printEuclerianPathCycle(self):
        res = self.euclerainPath()
        
        if res == 0:
            print("the graph is not euclerian.")
            logging.info("the graph is not euclerian.")
        elif res == 1:
            print("the graph has euclerian path.")
            logging.info("the graph has euclerian path.")
            self.printEuclerianPath()
        elif res == 2:
            print("the graph has euclerian path and cycle.")
            logging.info("the graph has euclerian path and cycle.")
            self.printEuclerianPath()
            
    # finally print the euclerian path
    def printEuclerianPath(self):
        if not self.isConnected():
            print("the graph is not connected.")
            logging.info("the graph is not connected.")
            return
        else:
            # find a odd vertex to start the printing
            start_vertex = None
            for i in self.vertices:
                if len(self.graph[i])%2 !=0:
                    start_vertex = i
                    break
            
            # if no odd vertices found then start with the any vertex
            if start_vertex is None:
                start_vertex = self.vertices[0]
                for i in self.vertices:
                    if len(self.graph[i])>0:
                        start_vertex = i
                        break
                    
            # heirHolzer algo 
            curr_path = [start_vertex]
            circuit = []
            
            while curr_path:
                curr_vertex = curr_path[-1]
                if self.graph[curr_vertex]:
                    next_vertex = self.graph[curr_vertex].pop()
                    self.graph[next_vertex].remove(curr_vertex)
                    curr_path.append(next_vertex)
                else:
                    circuit.append(curr_path.pop())
                
            # print the circuit for the path
            print('->'.join(circuit))
            logging.info('->'.join(circuit))
            
            
vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

g1 = Graph(vertices)
g1.addEdge('a', 'b')
g1.addEdge('a', 'g')
g1.addEdge('b', 'c')
g1.addEdge('b', 'f')
g1.addEdge('c', 'd')
g1.addEdge('d', 'e')
g1.addEdge('e', 'f')
g1.addEdge('f', 'g')


g1.printEuclerianPathCycle()