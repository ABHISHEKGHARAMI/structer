# setting up the min Heap
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()

# building the heap
class Heap:
    def __init__(self):
        self.heap = []
        
        
    # left
    def left(self,i):
        return 2 * i + 1
    
    # right
    def right(self,i):
        return 2 * i + 2
    
    # parent
    def parent(self,i):
        return (i - 1) // 2
    
    # heapify
    def heapify(self,i):
        largest = i 
        left = 2 *i + 1
        right = 2 * i + 2
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
            
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
            
        if i != largest:
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
            self.heapify(largest)
            
            
    # build heap
    def buildHeap(self,arr):
        for i in range(len(arr)):
            self.heap.append(arr[i])
        for i in range(len(self.heap)//2,-1,-1):
            self.heapify(i)
            
            
    # print the heap
    def printHeap(self):
        for i in self.heap:
            print(f"->{i}",end=" ")
            logging.info(f"->{i}")
            
            
            
arr = list(map(int,input("enter the array seperated by comma :").split(" ")))
h1 = Heap()
h1.buildHeap(arr)
h1.printHeap()