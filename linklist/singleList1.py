'''
Single list implementation for linked list using python.

there are several operation need to follow
 i. insert at the front d
 ii. insert at the end d
 iii. insert after a certain node
 iv. insert before a certain node
 v. delete from the front
 vi . delete from the end
 vii. delete after a certain node
 viii. delete before a certain node
 ix. print the list. d
 x . search from the list d
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
        print(f"\nInserting data {data} at the front .....\n")
        node = Node(data)
        node.next = self.head
        self.head = node
        
        
    # insert at the back end of the linked list
    def insertEnd(self,data):
        node = Node(data)
        print(f"\nInserting Data {data} at the end .....\n")
        if self.head is None:
            self.insertFront(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            
            
    # inserting after a certain node
    def insertAfterNode(self,data_after,data):
        if self.head is None:
            print("Can't Perform operation List is empty .")
        else:
            pass
            
    # searching in the list
    def search(self,data):
        flag = False
        if self.head is None:
            print("\nList is empty\n.")
        else:
            temp = self.head
            while temp:
                if temp.data == data:
                    flag = True
                    break
                temp = temp.next
        
        if flag == True:
            return True
        else:
            return False
            
    # printing the list
    def printingList(self):
        if self.head is None:
            print("The List is empty ..\n")
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
if list1.search(4) == True:
    print("Present")
else:
    print("Not Present.")
