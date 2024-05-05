# setting up for the logging ops
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


class PriorityQueue:
    def __init__(self):
        self.heap = []
        
    def parent(self):
        return (i - 1)//2
    
    def left(self,i):
        return 2 * i + 1
    
    def right(self,i):
        return 2 * i + 2
    
    def insertPQ(self,data):
        print(f"inserting the {data} in the priority queue.")
        logging.info(f"inserting the {data} in the priority queue.")
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self,i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)],self.heap[i] = self.heap[i],self.heap[self.parent(i)]
            i = self.parent(i)
            
    def extractMin(self):
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down(len(self.heap))
        return min_value
    
    def heapify_down(self,i):
        min_index = i
        left = self.left(i)
        right = self.right(i)
        if left < len(self.heap) and self.heap[self.parent(i)] > self.heap[left]:
            left = i
        if right < len(self.heap) and self.heap[self.parent(i)] > self.heap[right]:
            right = i
            
        if i != min_index:
            self.heap[i] ,self.heap[min_index] = self.heap[min_index] , self[i]
            self.heapify_down(min_index)
            
            
    def peekValue(self):
        if len(self.heap) == 0:
            print("the priority queue is empty.")
            logging.info("the priority queue is empty.")
            return None
        else:
            return self.heap[0]
            
            
            
    def printPQ(self):
        print("printing the priority queue.")
        logging.info("printing the priority queue.")
        if len(self.heap) == 0:
            print("the priority queue is empty.")
            logging.info("the priority queue is empty.")
        else:
            for i in self.heap:
                print(f"->{i}",end=" ")
                logging.info(f"->{i}")


# checking the priority queue
h1 = PriorityQueue()

arr = [5,3,8,2]

for i in arr:
    h1.insertPQ(i)   
    
h1.printPQ()
print(f"The most important task of the priority is : {h1.extractMin()}")
    
    

        
        