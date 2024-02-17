'''
Single list implementation for linked list using python.

there are several operation need to follow
 i. insert at the front
 ii. insert at the end
 iii. insert after a certain node
 iv. insert before a certain node
 v. delete from the front
 vi . delete from the end
 vii. delete after a certain node
 viii. delete before a certain node
 ix. print the list.
 and more ..
 one by one we will implement this.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# class for linked list
class linkedList:
    def __init__(self):
        self.head = None
        
    
    # inserting at the front of the Linked List
    def insertFront(self,data):
        print("Inserting data at the front .....")
        node = Node(data)
        node.next = self.head
        self.head = node
        
        
    # insert at the back end of the linked list
    def insertEnd(self,data):
        node = Node(data)
        print("Inserting Data at the end .....")
        if self.head is None:
            self.insertFront(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            
    # printing the list
    def printingList(self):
        if self.head is None:
            print("The List is empty ..")
        else:
            print("Printing List .......")
            temp = self.head
            while temp!= None:
                print(f"{temp.data}=>",end=" ")
                temp = temp.next
# testing the code
list1 = linkedList()

list1.insertFront(1)
list1.insertEnd(2)
list1.insertEnd(3)
list1.insertEnd(4)
list1.insertEnd(5)

list1.printingList()
