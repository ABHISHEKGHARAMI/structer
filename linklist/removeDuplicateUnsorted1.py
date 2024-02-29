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
    
    # remove the duplicate from the unsorted linked list
    def removeDupUnsorted(self):
        if self.head is None:
            print("\nthe list is empty.\n")
        else:
            temp = self.head
            dict1 = {}
            while temp:
                if temp.data in dict1:
                    dict1[temp.data] = dict1[temp.data] + 1
                else:
                    dict1[temp.data] = 1
                temp = temp.next
            #print(dict1)
            list2 = LinkedList()
            for i in dict1:
                list2.insertList(i)
            list2.printingList()
            
            
list1 = LinkedList()
list1.insertList(1)
list1.insertList(2)
list1.insertList(2)
list1.insertList(3)
list1.insertList(4)
list1.insertList(5)

list1.printingList()

list1.removeDupUnsorted()