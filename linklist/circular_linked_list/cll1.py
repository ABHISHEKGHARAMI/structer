#  attempting to create the circular linked list

# set up the log
import sys
sys.path.append("D:/python_exercise_geeks/structer-1")

from settings import setup_logging
import logging

setup_logging()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Clist:
    def __init__(self):
        self.head = None
        
    # inserting the node at the front of the linked list
    def insertFront(self,data):
        print(f"\nInserting the {data} at the front of the linked list .")
        logging.info(f"\nInserting the {data} at the front of the linked list .")
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head
            
    # insertion at the last
    def insertionlast(self,data):
        node = Node(data)
        print(f"\nInserting {data} at the end of the data.")
        logging.info(f"\nInserting {data} at the end of the data.")
        if self.head is None:
            self.insertFront(data)
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head
            
    
    # display the linked  list
    def display(self):
        print("\nPrinting the linked list.")
        logging.info("\nPrinting the linked list.")
        if self.head is None:
            print("\nthe list is empty.")
            logging.info("\nthe list is empty.")
        else:
            temp = self.head
            while True:
                print(f"{temp.data}=>", end=" ")
                logging.info(f"{temp.data}=>")
                temp = temp.next
                if temp == self.head:
                    break
                
                
                

# executing the basic function
clist = Clist()
clist.insertFront(1)
clist.insertionlast(2)
clist.insertionlast(3)
clist.insertionlast(4)
clist.insertionlast(5)
clist.display()

