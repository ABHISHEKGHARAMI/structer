# setting up the min Heap
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


class Heap:
    def __init__(self):
        self.heap = []
        
    def left(self,i):
        return 2 * i + 1
    
    def right(self,i):
        return 2 * i + 2
    
    def parent(self,i):
        return (i - 1)//2
    
    def heapify_up(self,i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i] :
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
    
    def insertHeap(self,data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)
        
        
    # function for the delete heap element
    def extractHeap(self):
        if len(self.heap) == 0:
            return
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down(0)
        return min_value
    
    
    # heapify down  function for the delete
    def heapify_down(self,i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left <len(self.heap) and self.heap[min_index] > self.heap[left]:
            min_index = left
        if right < len(self.heap) and self.heap[min_index] > self.heap[right]:
            min_index = right
            
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index] , self.heap[i]
            self.heapify_down(min_index)
        
    def print_heap(self):
        if len(self.heap) == 0:
            return
        else:
            for i in self.heap:
                print(i,end=" ")
                logging.info(i)
                
                
h1 = Heap()
while True:
    print("\n 0: Exit. \t1: Insert. \t2: Print Heap. \3: Extract heap.")
    choice = int(input("enter choice :"))
    if choice == 0:
        exit(0)
    elif choice == 1:
        data = int(input("enter the data to insert in the min heap."))
        h1.insertHeap(data)
        
    elif choice == 2:
        print("\nPrinting the heap.")
        logging.info("\nPrinting the heap.")
        h1.print_heap()
        
    elif choice == 3:
        min_value = h1.extractHeap()
        print(f"the min value extracted from the heap is : {min_value}")
        logging.info(f"the min value extracted from the heap is : {min_value}")
        
        
