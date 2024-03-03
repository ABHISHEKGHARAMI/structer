'''

There are two singly linked lists in a system. By some programming error, 

the end node of one of the linked lists got linked to the second list,

forming an inverted Y-shaped list. Write a program to get the point where two linked lists merge. 

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
                
                
    # length of the tree
    def length(self):
        return self.lengthUtil(self.head)
    
    # util function for the length
    def lengthUtil(self,node):
        if node is None:
            return 0
        else:
            return 1 + self.lengthUtil(node.next)
        
        
    # contain function
    
    def __contain__(self,data):
        if self.head is None:
            return 0
        else:
            flag = 0
            temp = self.head
            while temp:
                if temp.data == data:
                    flag = 1
                    break
                
                temp = temp.next
            if flag == 1:
                return 1
            else:
                return 0
        
        
# Intersection of two linked list.
def Intersection(list1,list2):
    m = list1.length()
    n = list2.length()
    flag = 1
    i_point = 0
    if m > n:
        temp1 = list2.head
        while temp1:
            if list1.__contain__(temp1.data) == 1:
                i_point = temp1.data
                break
            temp1 = temp1.next
    elif m == n:
        temp1 = list1.head
        while temp1:
            if list2.__contain__(temp1.data):
                i_point  = temp.data
                break
            temp1 = temp1.next
    else:
        temp1 = list1.head
        while temp1:
            if list2.__contain__(temp1.data) == 1:
                i_point = temp1.data
                break
            temp1 = temp1.next
    return i_point

# executing the main function
list1 = LinkedList()
list1.insertList(3)
list1.insertList(6)
list1.insertList(9)
list1.insertList(15)
list1.insertList(30)

list2 = LinkedList()
list2.insertList(10)
list2.insertList(15)
list2.insertList(30)

print(f"the intersection point of the two list is : {Intersection(list1,list2)}")
    