'''
Single list implementation for linked list using python.

there are several operation need to follow
 i. insert at the front
 ii. insert at the end
 iii. insert after a certain node
 iv. insert before a certain node
 v. delete from the front
 vi . delete from the end
 vii. delete after a certain node
 viii. delete before a certain node
 ix. print the list.
 and more ..
 one by one we will implement this.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
        
# class for link list
class LinkList:
    def __init__(self):
        self.head = None