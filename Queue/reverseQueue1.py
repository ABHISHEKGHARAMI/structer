'''

Description - Given an integer k and a queue of integers, 
we need to reverse the order of the first k elements of the queue,
leaving the other elements in the same relative order.
Only the following standard operations are allowed on the queue.
enqueue(x) : Add an item x to rear of queue
dequeue() : Remove an item from front of queue
size(( : Returns number of elements in queue.
front() : Finds front item.
'''

# set up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()

# class for the queue

class Queue:
    def __init__(self):
        self.queue = []
        
    # enqueue the element
    def enQueue(self,data):
        try:
            self.queue.append(data)
            print(f"{data} inserted in the queue.")
            logging.info(f"{data} inserted in the queue.")
        except Exception as e:
            logging.error(e)
            print(e)
            
    # dequeue the element
    def deQueue(self):
        try:
            if self.sizeQueue() == 0:
                print("The queue is under flowed.")
                logging.info("The queue is under flowed.")
            else:
                data = self.queue.pop(0)
                print(f"{data} is dequeued from the queue.")
                logging.info(f"{data} is dequeued from the queue.")
        except Exception as e:
            logging.error(e)
            print(e)
    
    # size of the queue
    def sizeQueue(self):
        try:
            if len(self.queue) == 0:
                return 0
            else:
                return len(self.queue)
        except Exception as e:
            logging.error(e)
            print(e)
            
    # front of the queue
    def frontQueue(self):
        if self.sizeQueue == 0:
            return -1
        else:
            return self.queue[0]
        
    # print the queue
    def printQueue(self):
        if self.sizeQueue() == 0:
            print("queue is empty.")
        else:
            print("printing Queue.")
            for i in self.queue:
                print(i,end=",")
            logging.info(self.queue)
        
q1 = Queue()
while True:
    print("\n1 :Enqueue. \n2: Dequeue. \n3. Size \n4: front Element \n5 : Print Queue. \n0: Exit.")
    choice = int(input("enter the choice:"))
    if choice == 1:
        data = int(input("enter the data :"))
        q1.enQueue(data)
    elif choice == 2:
        q1.deQueue()
    elif choice == 3:
        re = q1.sizeQueue()
        print(f"the size of the queue is : {re}")
        logging.info(f"the size of the queue is : {re}")
    elif choice == 4:
        re = q1.frontQueue()
        print(f"The front element of the queue is : {re}")
        logging.info(f"The front element of the queue is : {re}")
    elif choice == 5:
        q1.printQueue()
    elif choice == 0:
        exit(0)
    else:
        print("Wrong choice ..")
