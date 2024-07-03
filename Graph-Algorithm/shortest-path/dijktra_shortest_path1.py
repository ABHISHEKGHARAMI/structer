# setting up the logger for the repo.
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


# implementing the heap data structure for the dijkstra algo
class Heap:
    def __init__(self):
        self.heap = []
        
        
    # left child of the heap
    def left(self,i):
        return 2 * i + 1
    
    # right child of the heap
    def right(self,i):
        return 2 * i + 2
    # parent of any node
    def parent(self,i):
        return (i-1)//2
    
    # heapify up for the insertion of the new heap
    def heapify_up(self,i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)],self.heap[i] = self.heap[i],self.heap[self.parent(i)]
            i = self.parent(i)
            
    # insert the new data in the heap
    def insert(self,data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)
        
        
    # heapify down for the data to extract from the heap
    def pop(self):
        if len(self.heap) == 0:
            return
        min_index = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down(0)
        return min_index
    
    
    # heapify down for the pop operation
    def heapify_down(self,i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[min_index] > self.heap[left]:
            min_index = left
        if right < len(self.heap) and self.heap[min_index] > self.heap[right]:
            min_index = right
        if i != min_index:
            self.heap[i],self.heap[min_index] = self.heap[min_index],self.heap[i]
            self.heapify_down(min_index)
            
            
# graph data structure for the graph
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.v = len(self.vertices)
        self.index_map = {vertex : idx for idx,vertex in enumerate(self.vertices)}
        self.graph = { vertex : [] for vertex in self.vertices}
        
    # adding the edge between for the graph for the two vertex
    def addEdge(self,u,v,w):
        if u in self.index_map and v in self.index_map:
            self.graph[u].append((v,w))
        else:
            print(f"{u} or {v} not in the graph.")
            logging.info(f"{u} or {v} not in the graph.")
            
            
    # print the graph
    def printGraph(self):
        try:
            if not self.graph:
                print("Graph is empty.")
                logging.info("Graph is empty.")
            else:
                for vertex in self.graph:
                    print(f"{vertex}: ", end="")
                    for neighbor in self.graph[vertex]:
                        print(f"{neighbor} ", end="")
                    print()
                logging.info("Graph printed successfully.")
        except Exception as e:
            print(e)
            logging.info(e)
            
            
    # dijkstra's algorithm for the shortest path for the graph
    def dijkstra_shortest_path(self,start):
        pq = Heap()
        pq.insert((0,start))
        
        
        # assigning the vertex for infinity for the distance 
        distances = { vertex : 'infinity' for vertex in self.vertices}
        distances[start] = 0
        
        while len(pq.heap) > 0:
            current_distance , current_vertex = pq.pop()
            
            if current_distance > distances[current_vertex]:
                continue
            
            
            for neighbor,weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor] : 
                    distances[neighbor] = distance
                    pq.insert((distance,neighbor))
                    
        return distances
    
    
# execution for the shortest path of the graph
vertices = ['a','b','c','d']

g1 = Graph(vertices)

g1.addEdge('a', 'b', 1)
g1.addEdge('b', 'c', 3)
g1.addEdge('c', 'd', -2)
g1.addEdge('d', 'b', -3)


# print the graph
g1.printGraph()

#dijkstra's algorithm
distance = g1.dijkstra_shortest_path('a')

print("the shortest path of the graph :")
logging.info("the shortest path of the graph :")

print("vertex------distance")
print("--------------------")
logging.info("vertex------distance")
logging.info("--------------------")
for vertex in distance :
    print(f"{vertex}------------{distance[vertex]}")
    logging.info(f"{vertex}------------{distance[vertex]}")