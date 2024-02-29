'''
 Remove the duplicate from the linked list 
 
 Write a function that takes a list sorted in non-decreasing order and deletes any 
 duplicate nodes from the list. The list should only be traversed once. 
For example if the linked list is 11->11->11->21->43->43->60 then 
removeDuplicates() should convert the list to 11->21->43->60. 

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
    
    
    # remove duplicate from the linked list 
    def removeDuplicate(self):
        if self.head is None:
            print("\n\the list is empty.\n")
        else:
            print("\nprinting the list ...\n")
            temp = self.head
            while temp and temp.next.next:
                if temp.data == temp.next.data:
                    temp.next = temp.next.next
                temp = temp.next
                    


# executing the created function
list1 = LinkedList()
list1.insertList(1)
list1.insertList(2)
list1.insertList(2)
list1.insertList(3)
list1.insertList(4)
list1.insertList(5)

list1.printingList()

# executing the main function
list1.removeDuplicate()

list1.printingList()
