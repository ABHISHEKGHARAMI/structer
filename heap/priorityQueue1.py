# setting up for the logging ops
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(
                i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down(0)
        return min_val

    def heapify_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.heapify_down(min_index)

    def peek_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]


# Example usage:
pq = PriorityQueue()
pq.insert(5)
pq.insert(3)
pq.insert(8)
pq.insert(2)

print("Minimum element:", pq.peek_min())  # Output: 2

print("Extracted elements in order:")
while pq.peek_min() is not None:
    data = pq.extract_min()
    print(f"->{data}",end=" ")
    logging.info(f"->{data}")
    # Output: 2, 3, 5, 8

    
    

        
        