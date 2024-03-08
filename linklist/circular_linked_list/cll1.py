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
        
    # contain
    def __contain__(self,data):
        if self.head is None:
            return 0
        else:
            temp = self.head
            flag = 0
            while temp.next != self.head:
                if temp.data == data:
                    flag = 1
                    break
                temp = temp.next
            if flag == 1:
                return 1
            else:
                return 0
        
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
            
            
    # insertion after a certain given node
    def insertionAfterNode(self,data_after_insert,data_to_insert):
        node = Node(data_to_insert)
        if self.head is None:
            print("\nthe list is empty.")
            logging.info("\nthe list is empty.")
        else:
            if self.__contain__(data_after_insert) == 0:
                print(f"\n{data_after_insert} is not present in the list.")
                logging.info(f"\n{data_after_insert} is not present in the list.")
            else:
                print(f"\ninserting {data_to_insert} in the list.")
                logging.info(f"\ninserting {data_to_insert} in the list.")
                temp = self.head
                while temp.next != self.head:
                    if temp.data == data_after_insert:
                        temp.next = node
                        node.next = temp.next.next
                    temp = temp.next
            
    
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
clist.insertionAfterNode(3,6)
clist.display()

