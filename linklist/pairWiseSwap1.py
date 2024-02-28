'''Given a singly linked list, write a function to swap elements pairwise. 

Input : 1->2->3->4->5->6->NULL 
Output : 2->1->4->3->6->5->NULL

Input : 1->2->3->4->5->NULL 
Output : 2->1->4->3->5->NULL

Input : 1->NULL 
Output : 1->NULL 

For example, if the linked list is 1->2->3->4->5 then the function should change
it to 2->1->4->3->5, and if the linked list is then the function should change it to.  '''

# node for the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# linked list
class LinkedList:
    def __init__(self):
        self.head = None
        
    
    # insert the new node or append in the linked list
    def insertList(self,data):
        print("\ninserting the new data in the linked list ...\n")
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp:
                temp = temp.next
            temp.next = new_node
            
            
    # printing the linked list
    def printingList(self):
        if self.head is None:
            print("\nthe list is empty.....\n")
        else:
            temp = self.head
            while temp.next:
                print(f"{temp.data}=>",end=" ")
                temp = temp.next
            
            
