# setting up the logger

import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

# setting the Queue for the class
class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = len(self.queue) - 1
        
    # enQueue for the data
    def enQueueQueue(self,data):
        try:
            if self.front == self.rear:
                print("\nThe Queue is full.")
                logging.error("The Queue is full.")
            else:
                print("\nInserting the queue ...")
                self.queue.append(data)
                self.rear = self.rear + 1
                logging.info(f"Inserted {data} in the queue .")
                print(f"Inserted {data} in the queue .")
        except Exception as e:
            print(e)
            logging.error(e)
            
    # deQueue for the data
    def deQueue(self):
        try:
            if self.front == 0:
                print("The queue is empty.")
                logging.error("The queue is empty.")
            else:
                data = self.queue.pop(0)
                self.rear = self.rear - 1
                print(f"{data} is dequeued from the queue.")
                logging.info(f"{data} is dequeued from the queue.")
                
        except Exception as e:
            print(e)
            logging.error(e)
            
    # print the Queue
    def printQueue(self):
        try:
            if self.front == 0:
                print("The Queue is empty.")
                logging.info("The Queue is empty.")
            else:
                print("\nPrinting the queue ...")
                logging.info("\nPrinting the queue ...")
                for i in range(self.front,self.rear):
                    print(self.queue[i],end=" ")
        except Exception as e:
            print(e)
            logging.error(e)
            
q1 = Queue()           
while True:
    print("\n1: Enqueue. \n2: Dequeue \n3: Print Queue.")
    choice = int(input("\nEnter the choice :"))
    if choice == 1:
        data = int(input("Enter the data to enqueued :"))
        q1.enQueueQueue(data)
    elif choice == 2:
        q1.deQueue()
    elif choice == 3:
        q1.printQueue()
    else:
        print("Wrong choice !!")

        
            
    