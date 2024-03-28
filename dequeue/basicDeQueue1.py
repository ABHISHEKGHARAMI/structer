# set up the logger

import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging


setup_logging()
# setting up the dequeue
class Dequeue:
    def __init__(self):
        self.queue = []
        
    # left enqueue
    def leftEnqueue(self,data):
        try:
            self.queue.insert(0,data)
            logging.info(f"{data} inserted to the left of the queue.")
            print(f"{data} inserted to the left of the queue.")
        except Exception as e:
            print(e)
            logging.info(e)
            
    # right enqueue
    def rightEnqueue(self,data):
        try:
            self.queue.append(data)
            logging.info(f"{data} inserted to the right of the queue.")
            print(f"{data} inserted to the right of the queue.")
        except Exception as e:
            print(e)
            logging.error(e)
            
            
    # min value
    def minvalue(self):
        if len(self.queue) == 0:
            return -1
        else:
            return min(self.queue)
    
    # max value
    def maxvalue(self):
        if len(self.queue) == 0:
            return -1
        else:
            return max(self.queue)
    
    # dequeue from the left
    def leftDeque(self):
        if len(self.queue) == 0:
            print("the queue is empty.")
        else:
            data = self.queue.pop(0)
            print(f"{data} deleted from the queue from the left.")
            logging.info(f"{data} deleted from the queue from the left.")
    
    # dequeue from the right
    def rightDequeue(self):
        if len(self.queue) == 0:
            print("the queue is empty.")
        else:
            data = self.queue.pop()
            print(f"{data} deleted from the queue from the left.")
            logging.info(f"{data} deleted from the queue from the left.")
            
    # print the queue
    def printQueue(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            for i in self.queue:
                print(i,end=" ")
            logging.info(self.queue)
            
q1 = Dequeue()

while True:
    print("\n1: enqueue left. \n2: enqueue right. \n3: max value. \n4:min value. \n5: print queue.")
    print("\n6: dequeue left. \n7: dequeue right \n0: exit.")
    choice = int(input("enter choice :"))
    if choice == 1:
        data = int(input("enter data :"))
        q1.leftEnqueue(data)
    elif choice == 2:
        data = int(input("enter data :"))
        q1.rightEnqueue(data)
    elif choice == 3:
        print(f"The max value is : {q1.maxvalue()}")
        logging.info(f"The max value is : {q1.maxvalue()}")
    elif choice == 4:
        print(f"The min value is : {q1.minvalue()}")
    elif choice == 5:
        q1.printQueue()
    elif choice == 6:
        q1.leftDeque()
    elif choice == 7:
        q1.rightDequeue()
    elif choice == 0:
        exit(0)
    else:
        print("Wrong choice !!")
