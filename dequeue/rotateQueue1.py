'''
Rotate the queue by k .

'''
# setting up the logger .
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging


setup_logging()

# main function for the rotation
from collections import deque

def rotateQueue(q,k):
    try:
        q1 = deque(q)
        l1 = []
        for i in range(k):
            l1.append(q1.popleft())
        l1 = l1[::-1]
        for i in range(len(l1)):
            q1.appendleft(l1.pop())
        print(f"After queue rotation for the queue will be : {q1}")
        logging.info(f"After queue rotation for the queue will be : {q1}")
    except Exception as e:
        logging.error(e)
        print(e)
        
        
# execution for the main function
queue = [1 , 2, 3, 4, 5, 6, 7, 8, 9]
rotateQueue(queue,3)