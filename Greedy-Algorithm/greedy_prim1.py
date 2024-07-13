# setting up the logger file

import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


'''
problem statement :

the graph is supplied with the edges for the output will be the minimum spanning tree.

'''


class MinHeap:
    def __init__(self):
        self.heap = []

    # left child
    def left(self, i):
        return 2 * i + 1

    # right child
    def right(self, i):
        return 2 * i + 2

    # parent for the node
    def parent(self, i):
        return (i - 1) // 2

    # insert the data
    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap)-1)

    # extract the min from the heap
    def extractMin(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        else:
            root = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._heap_down_(0)

            return root

    # utility function for the heap up
    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(
                i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    # utility function for the heap down
    def _heap_down_(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            left = smallest

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            right = smallest

        if i != smallest:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heap_down_(smallest)

    # check the heap is empty or not

    def is_Empty(self):
        return len(self.heap) == 0


# graph structure for the prim algorithm
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.v = len(vertices)
        self.index_map = {vertex: idx for idx,
                          vertex in enumerate(self.vertices)}
        self.graph = {vertex: [] for vertex in self.vertices}

    # adding the edge of the undirected graph
    def addEdge(self, u, v, w):
        if u and v in self.vertices:
            self.graph[u].append((v, w))
            # reverse edge for the graph
            self.graph[v].append((u, w))
        else:
            print(f"{u} or {v} or both not added in the graph.")
            logging.info(f"{u} or {v} or both not added in the graph.")

    # print the graph
    def printGraph(self):
        try:
            if not self.graph:
                print("Graph is empty.")
                logging.info("Graph is empty.")
            else:
                print("Printing the graph.")
                logging.info("Printing the graph.")
                for vertex in self.graph:
                    print(f"{vertex}: ", end="")
                    for neighbor in self.graph[vertex]:
                        print(f"{neighbor} ", end="")
                    print()
                logging.info("Graph printed successfully.")
        except Exception as e:
            print(e)
            logging.info(e)

    # prim algo for the min spanning tree
    def primMST(self):
        start_vertex = self.vertices[0]

        # getting the min from the heap
        h1 = MinHeap()
        h1.insert((0, start_vertex))
        in_mst = set()
        mst_edges = []

        total_weight = 0

        while not h1.is_Empty() and len(in_mst) < self.v:
            weight, u = h1.extractMin()

            if u in in_mst:
                continue
            in_mst.add(u)
            total_weight += weight

            for v, w in self.graph[u]:
                if v not in in_mst:
                    h1.insert((w, v))
                    mst_edges.append((u, v, w))

        print("printing the edges with weight of the graph :")
        logging.info("printing the edges with weight of the graph :")

        for u, v, w in mst_edges:
            print(f"{u}---{v} : {w}")
            logging.info(f"{u}---{v} : {w}")
        print(f"total weight of the mst will be : {total_weight}")
        logging.info(f"total weight of the mst will be : {total_weight}")


# main execution of the program
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

# print the graph
g1.printGraph()

# now time for prim mst
g1.primMST()
