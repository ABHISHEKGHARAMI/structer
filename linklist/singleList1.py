'''
Single Link List implement in python
 different types of operation will learn in later like
 i . insert at the front,end,after or front of the node
 ii. delete node from the front,end , after or front of the node.
 iii. display all the nodes.
 
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
# class for the linked list
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    # insert at the front
    def insertFront(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
            
            
    # insert at the end of the linked list
    def insertEnd(self,data):
        if self.head is None:
            self.insertFront(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            new_node = Node(data)
            temp.next = new_node
            new_node.next = None
            
    # display the linked list
    def display(self):
        if self.head is None:
            print("the linked list is empty.")
        else:
            temp = self.head
            while temp.next :
                print(f"=>{temp.data}")
                temp = temp.next
            