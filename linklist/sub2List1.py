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