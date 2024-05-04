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
    def heapify(self,i,heap_size):
        largest = i 
        left = 2 *i + 1
        right = 2 * i + 2
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
            
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
            
        if i != largest:
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
            self.heapify(largest,heap_size)
            
            
    # build heap
    def buildHeap(self,arr):
        self.heap = arr[:]
        for i in range(len(self.heap)//2,-1,-1):
            self.heapify(i,len(arr))
            
    # heap sort
    def heap_sort(self):
        heap_size = len(self.heap)
        for i in range(heap_size-1,0,-1):
            self.heap[0],self.heap[i] = self.heap[i] , self.heap[0]
            heap_size -= 1
            self.heapify(i,heap_size)
            
            
    # print the heap
    def printHeap(self):
        for i in self.heap:
            print(f"->{i}",end=" ")
            logging.info(f"->{i}")
            
            
            
def heapSort(arr):
    h1 = Heap()
    h1.buildHeap(arr)
    h1.heap_sort()
    return h1.heap

arr = list(map(int,input("enter the data for list with space :").split(" ")))
sorted_arr = heapSort(arr)

print(f"After heap sort is the list is : {sorted_arr}")
logging.info(f"After heap sort is the list is : {sorted_arr}")