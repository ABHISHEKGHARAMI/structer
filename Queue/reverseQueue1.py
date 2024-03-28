'''
Given an integer K and a queue of integers, we need to reverse the order 
of the first K elements of the queue, leaving the other elements in the same relative order.

'''
# set up for the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()
from collections import deque
# function for the reverse the queue using the deque
def reverseQueue(q,k):
    q1 = deque(q)
    mem = []
    for i in range(k):
        mem.append(q1.popleft())
    logging.info(f"After deque the list is :{mem}")
    mem = mem[::-1]
    for i in mem:
        q1.appendleft(mem.pop())
        
    print(f"After the operation the queue is :{q1}")
    logging.info(f"After the operation the queue is :{q1}")



# execution of the main program
q = [1,2,3,4,5]
reverseQueue(q,3)    
    