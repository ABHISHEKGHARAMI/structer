# minus of two list
'''Given two linked lists that represent two large positive numbers. Subtract the smaller number
from the larger one and return the difference as a linked list. 
Note that the input lists may be in any order, but we always need to subtract smaller ones 
from larger ones.
Note: It may be assumed that there are no extra leading zeros in input lists.

Examples: 

Input: l1 = 1 -> 0 -> 0 -> NULL,  l2 = 1 -> NULL
Output: 0->9->9->NULL
Explanation: Number represented as 
lists are 100 and 1, so 100 - 1 is 099
Input: l1 = 7-> 8 -> 6 -> NULL,  l2 = 7 -> 8 -> 9 NULL
Output: 3->NULL
Explanation: Number represented as 
lists are 786 and  789, so 789 - 786 is 3, 
as the smaller value is subtracted from 
the larger one. '''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    # insert the list
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
            
            
    # print the list
    def printList(self):
        if self.head is None:
            print("\nthe list is empty.\n")
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" ")
                temp = temp.next
                
                
    # reverse the list
    def reverseList(self):
        if self.head is None:
            print("\nthe list is empty.\n")
        else:
            prev = None
            temp = self.head
            while temp:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            self.head = prev
            
            
                
                
    # substraction of 2 lists
    def sub2List(self,list1,list2):
        borrow = 0 
        result = LinkedList()
        ptr1 = list1.head
        ptr2 = list2.head
        while ptr1 or ptr2:
            val1 = ptr1.data if ptr1 else 0
            val2 = ptr2.data if ptr2 else 0
            diff = val1 - val2 - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result.insertList(diff)
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
            
        return result
    
    
# testing the substraction result
list1 = LinkedList()
list1.insertList(1)
list1.insertList(2)
list1.insertList(0)


list2 = LinkedList()
list1.insertList(1)
list1.insertList(0)
list1.insertList(0)


#reverse the list
list1.reverseList()
list2.reverseList()

result = LinkedList().sub2List(list1,list2)

result.reverseList()

result.printList()
            
            