'''

Number is represented in linked list such that each digit corresponds to a node in linked list.
Add 1 to it. For example 1999 is represented as (1-> 9-> 9 -> 9) and adding 1 to 
it should change it to (2->0->0->0) 

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
# linkked list
class Linkedlist:
    def __init__(self):
        self.head = None
        
        
    # insert the data for the linked list
    def insertList(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            
    # display the node
    def displayList(self):
        if self.head is None:
            print("\nthe list is empty.\n")
        else:
            temp = self.head
            while temp:
                print(f"{temp.data}=>",end=" ")
                temp = temp.next
                
    # reverse the list
    def reverseList(self):
        if self.head is None:
            print("the list is empty.")
        else:
            prev = None
            temp = self.head
            while temp:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            self.head = prev


# testing the function build
list1 = Linkedlist()

list1.insertList(1)
list1.insertList(2)
list1.insertList(3)
list1.displayList()
list1.reverseList()
list1.displayList()
            