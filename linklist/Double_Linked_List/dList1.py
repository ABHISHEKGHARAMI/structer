# basic operation on the linked list .
import sys
sys.path.append("D:/python_exercise_geeks/structer-1")

from settings import setup_logging
import logging





setup_logging()

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
            logging.info("\nPrinting data ......\n")
            temp = self.head
            while temp:
                print(f"{temp.data}=>",end=" ")
                logging.info(f"{temp.data}=>")
                
                temp = temp.next
                
                
    # add node to the front of the list
    def frontInsert(self,data):
        new_node = Node(data)
        new_node.prev = None
        print(f"\nInserting {data} at the front of the linked list .\n")
        logging.info(f"\nInserting {data} at the front of the linked list .\n")
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
            
    # checking any data is present or not
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
            
            
    # add data to the last of the linked list .
    def insertLast(self,data):
        new_node = Node(data)
        new_node.prev = None
        if self.head is None:
            self.frontInsert(data)
        else:
            print(f"\nInserting {data} at the end of the linked list .\n")
            logging.info(f"\nInserting {data} at the end of the linked list .\n")
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            
    # adding a new node after a given node
    def insertAfterNode(self,data_to_insert,data_after_insert):
        new_node = Node(data_to_insert)
        new_node.prev = None
        if self.head is None:
            print("\nThe list is empty.\n")
            logging.info("\nThe list is empty.\n")
        else:
            temp = self.head
            while temp:
                if temp.data == data_after_insert:
                    new_node.prev = temp
                    new_node.next = temp.next
                    if temp.next:
                        temp.next.prev = new_node
                    temp.next = new_node
                    return
                temp = temp.next
                
    # add before the given  data
    def insertBeforeData(self,data_to_insert,data_before_insert):
        new_node = Node(data_to_insert)
        new_node.prev = None
        if self.head is None:
            print("\nThe list is empty.\n")
            logging.info("\nThe list is empty.\n")
        else:
            if self.searchList(data_before_insert) == 0:
                print(f"\n{data_before_insert} is not present in the list .\n")
                logging.info(f"\n{data_before_insert} is not present in the list .\n")
            else:
                print(f"{data_to_insert} inserting in linked list .")
                logging.info(f"{data_to_insert} inserting in linked list .")
                temp = self.head
                while temp:
                    if temp.next.data == data_before_insert:
                        new_node.prev = temp
                        new_node.next = temp.next
                        temp.next.prev = new_node
                        temp.next = new_node
                        return
                    temp = temp.next
                    
    # delete the first node of the Double linked list
    def deleteList(self):
        print("\ndeleting the first node of the double linked list .\n")
        logging.info("\ndeleting the first node of the double linked list .\n")
        if self.head is None:
            print("\nThe double linked list is empty.\n")
            logging.info("\nThe double linked list is empty.\n")
        elif self.head.next is None:
            temp = self.head
            print(f"{temp.data} is deleted .")
            logging.info(f"{temp.data} is deleted .")
            self.head = None
        else:
            temp = self.head
            self.head = self.head.next
            print(f"{temp.data} deleted from the double linked list.")
            logging.info(f"{temp.data} deleted from the double linked list.")
            
    # delete the last node of the double linked list
    def deleteLastNode(self):
        print("\ndeleting the last node of the double linked list ..\n")
        logging.info("\ndeleting the last node of the double linked list ..\n")
        if self.head is None:
            print("\nthe linked list is empty ..\n")
            logging.info("\nthe linked list is empty ..\n")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None
            
    
    # delete after a certain node after a given node data
    def deleteAfterNodeData(self,data_after_invoke):
        print(f"\nAfter {data_after_invoke} data to be deleted.")
        if self.head is None:
            print("\nThe Double Linked list is empty can't perform operation ..\n")
        else:
            temp = self.head
            while temp:
                if temp.data == data_after_invoke:
                    temp.next = temp.next.next
                temp = temp.next
            
    
    
    # delete before the node given
    def deleteBeforeNode(self,data_before_invoke):
        print(f"\n{data_before_invoke} before data deleting operation...\n")
        if self.head is None:
            print("\n\The list is empty.\n")
        else:
            pass
        
        
    # delete a certain data
    def deleteNode(self,data):
        if self.head is None:
            print("\nThe Double Linked list is empty can't perform operation ..\n")
        else:
            print(f"\n{data} deleting from the list ..\n")
            temp = self.head
            while temp:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    return
                temp = temp.next
            
            
    
    # reverse the double linked list
    def reverseList(self):
        print("\nReversing the double linked list ..\n")
        if self.head is None or self.head.next is None:
            print("\nThe current double linked list is empty or has single element no need to reverse it .\n")
        else:
            print("\nReversing the Double Linked List ..\n")
            current = self.head
            prev_node = None
            while current is not None:
                temp = current.next
                current.next = prev_node
                current.prev = temp
                
                #  now move the current node
                prev_node = current
                current = temp
            # set up the prev node to the head
            self.head = prev_node
    
          
    # search the data to the dll
    def searchList(self,data):
        if self.head is None:
            print("\nThe list is empty can't find the data in the list .\n")
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
            
    # find the length of the tree
    def lengthList(self):
        return self.lengthUtill(self.head)
    
    
    # util function for the  length function
    def lengthUtill(self,node):
        if node is None:
            return 0
        else:
            return 1 + self.lengthUtill(node.next)
        
        
    # finding the middle of the node
    def middleNode(self):
        if self.head is None:
            print("\nThe list is empty.\n")
            return 0
        else:
            temp = self.head
            data = 0
            count = 0
            while temp:
                if count == (self.lengthList())//2:
                    data = temp.data
                    break
                count += 1
                temp = temp.next
            return data
        
        
        
# executing the linked list
dlist1 = dList()
dlist1.frontInsert(1)
dlist1.insertLast(2)
dlist1.insertLast(3)
dlist1.insertLast(4)
dlist1.display()
dlist1.searchList(3)
dlist1.insertAfterNode(6,3)
dlist1.display()
dlist1.insertBeforeData(7,3)
dlist1.display()
dlist1.deleteList()
dlist1.display()
dlist1.deleteLastNode()
dlist1.display()
dlist1.deleteAfterNodeData(7)
dlist1.display()
print(f"The length of the Double linked list is : {dlist1.lengthList()}")
print(f"The data of the middle of the node is : {dlist1.middleNode()}")
dlist1.reverseList()
dlist1.display()
data = int(input("enter the data in the terminal to be deleted :"))
if dlist1.__contain__(data) == 1:
    dlist1.deleteNode(data)
    dlist1.display()
else:
    print(f"\n{data} is not present in the double linked list .\n")
