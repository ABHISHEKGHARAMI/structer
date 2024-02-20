'''
Single list implementation for linked list using python.

there are several operation need to follow
 i. insert at the front d
 ii. insert at the end d
 iii. insert after a certain node d
 iv. insert before a certain node d
 v. delete from the front d
 vi . delete from the end d
 vii. delete after a certain node d
 viii. delete before a certain node d
 ix. print the list. d
 x . search from the list d
 xi . find the length the list
 xii . Reverse the linked list .
 xiii . Middle of the Linked List .
 and more ..
 one by one we will implement this.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# class for linked list
class linkedList:
    def __init__(self):
        self.head = None
        
    
    # inserting at the front of the Linked List
    def insertFront(self,data):
        print(f"\nInserting data {data} at the front .....\n")
        node = Node(data)
        node.next = self.head
        self.head = node
        
        
    # insert at the back end of the linked list
    def insertEnd(self,data):
        node = Node(data)
        print(f"\nInserting Data {data} at the end .....\n")
        if self.head is None:
            self.insertFront(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            
            
    # inserting after a certain node
    def insertAfterNode(self,data_after,data):
        if self.head is None:
            print("\nCan't Perform operation List is empty .\n")
        else:
            # just checking that the node exist in the list if exist then do the insertion .
            if self.search(data_after) == True:
                print(f"\n Inserting {data} after {data_after} ......\n")
                node = Node(data)
                temp = self.head
                while temp:
                    if temp.data == data_after:
                        node.next = temp.next
                        temp.next = node
                        break
                    temp = temp.next
                    
    
    # inserting after a certain given data
    def insertbefore(self,data_before,data):
        if self.search(data_before) == False:
            print("\ncan't insert the data , the node before insertion is not present ...")
        else:
            print(f"\nInserting the {data} before the given data {data_before}.\n")
            node = Node(data)
            temp = self.head
            prev = None
            while temp!= None:
                if temp.data == data_before:
                    if prev is None:
                        node.next = self.head
                        self.head = node
                    else:
                        node.next = temp
                        prev.next = node
                        break
                prev = temp 
                temp = temp.next
                
                
    
    # delete node from the front
    def deleteFront(self):
        if self.head is None:
            print("\nthe list is empty already.")
        else:
            temp = self.head
            self.head = self.head.next
            print(f"\nthe front data {temp.data} is deleted .")        
            
            
            
            
    # deleting data from the end of the list
    def deleteEnd(self):
        if self.head is None:
            print("\nthe list is empty already.")
        elif self.head.next is None:
            self.head  = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
        
    
    # delete data after a node given
    def deleteAfter(self,data_After):
        if self.search(data_After) == False:
            print("\n Can't delete data after the node.\n")
        else:
            if self.head == None:
                print("\n List is empty ..\n")
            elif self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next:
                    if temp.data == data_After:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                    
                    
    # delete before of a node, given data
    def deleteBefore(self,data_before):
        if self.head is None:
            print("\nThe list is empty can't delete.\n")
        elif self.head.next.data == data_before:
            self.head = self.head.next
        else:
            prev = None
            current = self.head
            while current.next :
                if current.next.data == data_before:
                    if prev is None:
                        self.head = current.next
                    else:
                        prev.next = current.next
                    break
                prev = current
                current = current.next
                
                
                
    # find the length of the list
    def lengthList(self):
        return self.findlengthrecurr(self.head)
    
    def findlengthrecurr(self,node):
        if node is None:
            return 0
        else:
            return 1 + self.findlengthrecurr(node.next)
        
        
        
    # Reverse the Linked list.
    def reverseList(self) :
        if self.head is None:
            print("\nthe linked list is empty so no reverse..\n")
        else:
            print("\nreversing the linked list.....\n")
            current = self.head
            prev = None
            while current is not None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            self.head = prev
            
            
            
            
    # Middle of the Linked List
    def middleList(self):
        if self.head == None:
            print("\n0\n")
        else:
            h = self.lengthList()
            h = h//2
            count = 0 
            temp = self.head
            while temp:
                if count == h:
                    print(f"\nthe middle of the list is :{temp.data}.\n")
                    break
                count += 1
                temp = temp.next
            
            
        
        
        
        
    # searching in the list
    def search(self,data):
        flag = False
        if self.head is None:
            print("\nList is empty\n.")
        else:
            temp = self.head
            while temp:
                if temp.data == data:
                    flag = True
                    break
                temp = temp.next
        
        if flag == True:
            return True
        else:
            return False
            
    # printing the list
    def printingList(self):
        if self.head is None:
            print("\nThe List is empty ..\n")
        else:
            print("\nPrinting List .......\n")
            temp = self.head
            while temp!= None:
                print(f"{temp.data}=>",end=" ")
                temp = temp.next
# testing the code
list1 = linkedList()

list1.insertFront(1)
list1.insertEnd(2)
list1.insertEnd(3)
list1.insertEnd(4)
list1.insertEnd(5)

list1.printingList()
if list1.search(4) == True:
    print("Present")
else:
    print("Not Present.")
    
    
#executing the insert after function
list1.insertAfterNode(3,6)
list1.printingList()
list1.insertbefore(2,7)
list1.printingList()
list1.deleteFront()
list1.printingList()
list1.deleteEnd()
list1.printingList()
list1.deleteAfter(3)
list1.printingList()
list1.deleteBefore(3)
list1.printingList()
print(f"\nThe length of the list is : {list1.lengthList()}")

list1.reverseList()
list1.printingList()
list1.middleList()

