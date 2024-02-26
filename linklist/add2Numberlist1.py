# add two number of the linked list and print the new linked list
'''
Given two numbers represented by two lists, write a function that returns the sum 
in the form of a linked list.

Example:

Input: 
List1: 5->6->3 // represents number 563 
List2: 8->4->2 // represents number 842 
Output: 
Resultant list: 1->4->0->5 // represents number 1405 
Explanation: 563 + 842 = 1405

Input: 
List1: 7->5->9->4->6 // represents number 75946
List2: 8->4 // represents number 84
Output: 
Resultant list: 7->6->0->3->0// represents number 76030
Explanation: 75946+84=76030

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# linked list for the node
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    # printing the linked list .
    def printingList(self):
        print("\nprinting the linked list...\n")
        if self.head is None:
            print("\nList is empty.\n")
        else:
            temp = self.head
            while temp:
                print(f"{temp.data}=>",end=" ")
                temp = temp.next
                
    # insert the data for the linked list
    def insertList(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            # append the data
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            
            
    # reverse the list
    def reverseList(self):
        if self.head is None:
            print("\nThe list is empty.\n")
        else:
            prev = None
            temp = self.head
            while temp:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            self.head = prev
                
# testing the list
list1 = LinkedList()
list1.insertList(1)
list1.insertList(2)
list1.insertList(3)
list1.insertList(4)
list1.printingList()
list1.reverseList()
list1.printingList()