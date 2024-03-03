'''

Given a linked list, rearrange it such that the converted list should be of the form a < b > c < d > e < f … where a, b, c… are consecutive data nodes of the linked list.

Examples: 

Input:  1->2->3->4
Output: 1->3->2->4 
Explanation : 1 and 3 should come first before 2 and 4 in zig-zag fashion, So resultant linked-list will be 1->3->2->4. 

Input:  11->15->20->5->10
Output: 11->20->5->15->10 

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
                
    
    # zig zag function
    def zigZag(self):
        pass