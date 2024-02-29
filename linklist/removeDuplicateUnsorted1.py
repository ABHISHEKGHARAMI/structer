'''
Given an unsorted Linked List, the task is to remove duplicates from the list. 

Examples:

Input: linked_list = 12 -> 11 -> 12 -> 21 -> 41 -> 43 -> 21 
Output: 12 -> 11 -> 21 -> 41 -> 43 
Explanation: Second occurrence of 12 and 21 are removed.

Input: linked_list = 12 -> 11 -> 12 -> 21 -> 41 -> 43 -> 21 
Output: 12 -> 11 -> 21 -> 41 -> 43 

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list


class LinkedList:
    def __init__(self):
        self.head = None

    # insert the new node or append in the linked list
    def insertList(self, data):
        print("\ninserting the new data in the linked list ...\n")
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # printing the linked list

    def printingList(self):
        if self.head is None:
            print("\nthe list is empty.....\n")
        else:
            print("\nprinting the list ...\n")
            temp = self.head
            while temp.next:
                print(f"{temp.data}=>", end=" ")
                temp = temp.next
    