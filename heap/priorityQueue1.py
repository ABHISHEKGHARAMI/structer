# setting up for the logging ops
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


class PQ:
    def __init__(self):
        self.heap = []
        
    def parent(self,i):
        return (i-1)//2
    
    def left(self,i):
        return 2 * i + 1
    
    
    def right(self,i):
        return 2 * i + 2
    
    
    def insertPQ(self,x):
        self.heap.append(x)
        self.heapify_up(len(self.heap))
        
    def heapify_up(self,i):
        while i > 0 and self.heap[self.parent(i)]<self.heap[i]:
            self.heap[self.parent( i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
            
            
    def extractHeap(self):
        if len(self.heap) == 0:
            return None
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down(0)
        return min_value
    
    
    def heapify_down(self,i):
        min_val = i
        left = self.left(i)
        right = self.right(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[min_val]:
            min_val = left
            
        if right < len(self.heap) and self.heap[right] < self.heap[min_val]:
            min_val = right
            
        if i != min_val:
            self.heap[i] , self.heap[min_val] = self.heap[min_val] , self.heap[i]
            self.heapify_down(min_val)
            
            
    def peek_value(self):
        if len(self.heap) == 0:
            return None
        else:
            return self.heap[0]
        
        
    def printPQ(self):
        if len(self.heap) == 0:
            print("priority queue is empty.")
            logging.info("priority queue is empty.")
        else:
            for i in self.heap:
                print(i,end=" ")
                logging.info(i)
        
        
pq = PQ()

pq.insertPQ(5)
pq.insertPQ(3)
pq.insertPQ(8)
pq.insertPQ(2)

pq.printPQ()
    
        
        