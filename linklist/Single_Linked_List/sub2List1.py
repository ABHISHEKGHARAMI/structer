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
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list implementation


class LinkedList:
    def __init__(self):
        self.head = None

    # Print the linked list
    def printingList(self):
        print("\nPrinting the linked list...\n")
        if self.head is None:
            print("\nList is empty.\n")
        else:
            temp = self.head
            while temp:
                print(f"{temp.data}=>", end=" ")
                temp = temp.next

    # Insert data into the linked list
    def insertList(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            # Append the data
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Reverse the list
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

    # Subtract two linked lists
    def subtractLinkedLists(self, list1, list2):
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


# Testing the linked list
list1 = LinkedList()
list1.insertList(1)
list1.insertList(0)
list1.insertList(0)

list2 = LinkedList()
list2.insertList(9)
list2.insertList(9)

# Reverse the lists
list1.reverseList()
list2.reverseList()

# Subtract the lists
result = LinkedList().subtractLinkedLists(list1, list2)

# Reverse the result list back to original order
result.reverseList()

# Print the result
result.printingList()

            
            