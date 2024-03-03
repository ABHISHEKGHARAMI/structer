# basic operation on the linked list .
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
        
# linked list
class dList:
    def __init__(self):
        self.head = None
        
    # display of the linked list
    def display(self):
        if self.head is None:
            print("\nThe list is empty.\n")
        else:
            print("\nPrinting data ....\n")
            temp = self.head
            while temp:
                print(f"{temp.data}=>",end=" ")
                
                temp = temp.next
                
                
    # add node to the front of the list
    def frontInsert(self,data):
        new_node = Node(data)
        new_node.prev = None
        print(f"\nInserting {data} at the front of the linked list .\n")
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
            
    # add data to the last of the linked list .
    def insertLast(self,data):
        new_node = Node(data)
        new_node.prev = None
        if self.head is None:
            self.frontInsert(data)
        else:
            print(f"\nInserting {data} at the end of the linked list .\n")
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        
        
        
# executing the linked list
dlist1 = dList()
dlist1.frontInsert(1)
dlist1.insertLast(2)
dlist1.insertLast(3)
dlist1.insertLast(4)
dlist1.display()