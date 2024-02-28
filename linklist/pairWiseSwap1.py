'''Given a singly linked list, write a function to swap elements pairwise. 

Input : 1->2->3->4->5->6->NULL 
Output : 2->1->4->3->6->5->NULL

Input : 1->2->3->4->5->NULL 
Output : 2->1->4->3->5->NULL

Input : 1->NULL 
Output : 1->NULL 

For example, if the linked list is 1->2->3->4->5 then the function should change
it to 2->1->4->3->5, and if the linked list is then the function should change it to.  '''

# node for the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# linked list
class LinkedList:
    def __init__(self):
        self.head = None
