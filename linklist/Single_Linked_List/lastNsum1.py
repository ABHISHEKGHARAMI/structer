'''
Given a linked list and a number n. Find the sum of the last n nodes of the linked list.
Constraints: 0 <= n <= number of nodes in the linked list.

Examples:  

Input : 10->6->8->4->12, n = 2
Output : 16
Sum of last two nodes:
12 + 4 = 16

Input : 15->7->9->5->16->14, n = 4
Output : 44
'''


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
            
            
    # length of the linked list
    def length(self):
        return self.lengthUtill(self.head)
    
    #util function
    def lengthUtill(self,node):
        if node is None:
            return 0
        else:
            return 1 + self.lengthUtill(node.next)
        
    # sum of the last n node
    def sumNnode(self,n):
        sum = 0
        len = self.length()
        start = len - n
        count  = 0
        if self.head is None:
            return 0
        else:
            temp = self.head
            while temp:
                if count >= start :
                    sum += temp.data
                    
                count += 1
                    
                temp = temp.next
            return sum

# testing the main function
link1 = LinkedList()
link1.insertList(1)
link1.insertList(2)
link1.insertList(3)
link1.insertList(4)
link1.insertList(5)
link1.insertList(6)

link1.printingList()
print(f"the length of the linked list is : {link1.length()}")

n = int(input("\nenter the number from the last  to get the sum :"))

print(f"\nThe sum of {n} is : {link1.sumNnode(n)}")
