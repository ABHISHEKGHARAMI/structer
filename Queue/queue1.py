# setting up the logger

import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

# setting the Queue for the class
class Queue:
    def __init__(self,size):
        self.size = size
        self.queue = []
        self.front = 0
        self.rear = 0
        
    # enQueue for the queue 
    def enQueue(self,data):
        if self.rear == self.size:
            print("The queue is empty.")
            logging.error("The queue is empty.")
        else:
            self.queue.append(data)
            self.rear += 1
            print(f"{data} is inserted.")
            logging.info(f"{data} is inserted.")
            
    # dequeue for the queue
    def deQueue(self):
        if self.rear == 0:
            print("The list is empty.")
            logging.error("The list is empty.")
        else:
            data = self.queue.pop(0)
            self.rear = self.rear - 1
            print(f"{data} is dequeued from the queue.")
            logging.info(f"{data} is dequeued from the queue.")
            
    # print the queue.
    def printQueue(self):
        if self.rear == 0:
            print("The list is empty.")
            logging.error("List is empty.")
        else:
            print("printing the queue :")
            for i in range(self.size):
                print(self.queue[i])
            logging.info(self.queue)

size = int(input("enter the size of queue :"))
q1 = Queue(size)
while True:
    print("\n1: enqueue. \n2: dequeue. \n3: print queue. \n0: exit.")
    choice = int(input("enter the choice :"))
    if choice == 1:
        data = int(input("enter the data :"))
        q1.enQueue(data)
    elif choice == 2:
        q1.deQueue()
    elif choice == 3:
        q1.printQueue()
    elif choice == 0:
        exit(0)
    else:
        print("Wrong choice !!!")
        