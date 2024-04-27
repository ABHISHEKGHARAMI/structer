# practice for binary tree
# set up the logger

import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


# queue
class Queue:
    def __init__(self):
        self.queue = []
        
        
    # push for the queue
    def push(self,data):
        self.queue.append(data)
    # pop for the queue
    def pop(self):
        if self.emptyqueue() == 1:
            print("queue is underflowed.")
            return -1
        else:
            data = self.queue.pop(0)
           # print(f"{data} is popped from the queue.")
            logging.info(f"{data} is popped from the queue.")
            return data
    
    # check queue
    def top(self):
        if  self.emptyqueue() == 1:
            return -1
        else:
            return self.queue[-1]
    def front(self):
        if self.emptyqueue() == 1:
            return -1
        else:
            return self.queue[0]
    
    # check empty or not
    def emptyqueue(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.horizontal_distance = 0
        
class Tree:
    def __init__(self):
        self.root = None
        
    # insert the data in the tree
    def insertTree(self,data):
        print(f"Inserting the {data} in the tree.")
        logging.info(f"Inserting the {data} in the tree.")
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.insert_recursive(self.root,data)
            
            
    # insert the recursive for the tree
    def insert_recursive(self,node,data):
        try:
            if node.data < data:
                if not node.right:
                    node.right = TreeNode(data)
                else:
                    self.insert_recursive(node.right,data)
            else:
                if not node.left:
                    node.left = TreeNode(data)
                else:
                    self.insert_recursive(node.left,data)
        except Exception as e:
            print(e)
            logging.error(e)
            raise Exception         
        
        
    # find the height
    def height(self,node):
        try:
            if not node:
                return 0
            else:
                lheight = self.height(node.left)
                rheight = self.height(node.right)
                return max(lheight,rheight) + 1
        except Exception as e:
            print(e)
            logging.error(e)
            raise Exception 
        
    # find the min value for the tree
    def find_min(self,node):
        if not node:
            return
        else:
            while node.left:
                node = node.left
            return node.data
        
    
    # delete the node for the tree
    def deleteNode(self,data):
        print(f"Delete {data} from the tree.")
        logging.info(f"Delete {data} from the tree.")
        self.deleteNode_recursive(self.root,data)
        
        
    # delete recursive for the tree
    def deleteNode_recursive(self,node,data):
        try:
            if not node or not data:
                return node
            else:
                if node.data < data:
                    node.right = self.deleteNode_recursive(node.right,data)
                elif node.data > data:
                    node.left = self.deleteNode_recursive(node.left,data)
                else:
                    if not node.left:
                        return node.right
                    elif not node.right:
                        return node.left
                    else:
                        temp_node = self.find_min(node.right)
                        node.data = temp_node.data
                        node.right = self.deleteNode_recursive(node.right,temp_node.data)
                return node
                        
        except Exception as e:
            print(e)
            logging.error(e)
            raise Exception
        
    # search for the tree
    def searchTree(self,node,data):
        if not node:
            return False
        else:
            if node.data == data:
                return  True
            elif node.data < data:
                return self.searchTree(node.right,data)
            else:
                return self.searchTree(node.left,data)
            
            
    #Traversal for the tree
    def inorder_traversal(self):
        if self.root:
            self.inorder_recur(self.root)
            
    # recursive
    def inorder_recur(self,node):
        if not node:
            self.inorder_recur(node.left)
            print(f"->{node.data}")
            logging.info(f"->{node.data}")
            self.inorder_recur(node.right)
    
    # traversal for the post order      
    def postorder(self):
        if self.root:
            self.postorder_recur(self.root)
            
    # recur
    def postorder_recur(self,node):
        if node:
            self.postorder_recur(node.left)
            self.postorder_recur(node.right)
            print(f"->{node.data}")
            logging.info(f"->{node.data}")
            
    # pre order traversal
    def preOrder(self):
        self.preorder_recur(self.root)
        
    # recur function
    def preorder_recur(self,node):
        if node:
            print(f"->{node.data}",end=" ")
            logging.info(f"{node.data}")
            self.preorder_recur(node.left)
            self.preorder_recur(node.right)
            
            
    # print the node from the k nodes
    def print_kth(self,k):
        self.print_kth_recur(self.root,k)
        
    # recur util function for that
    def print_kth_recur(self,node,k):
        if not node or k < 0:
            return 
        if k == 0 :
            print(f"->{node.data}",end=" ")
            logging.info(f"{node.data}",end=" ")
        self.print_kth_recur(node.left,k-1)
        self.print_kth_recur(node.right,k-1)
        
        
    
    # print the level order traversal
    def levelOrder(self):
        if self.root == None:
            return
        q1 = Queue()
        q1.push(self.root)
        while q1.emptyqueue() !=1:
            node_queue = q1.queue[0]
            print(f"->{node_queue.data}",end=" ")
            logging.info(f"->{node_queue.data}")
            q1.pop()
            if node_queue.left:
                q1.push(node_queue.left)
            if node_queue.right:
                q1.push(node_queue.right)
                
    # size of the tree
    def size(self,node):
        if node is None:
            return 0
        else:
            return self.size(node.left) + 1 + self.size(node.right)
        
        
    # get the max number
    def maxTree(self,node):
        if node == None:
            return -sys.maxsize
        res = node.data
        lres= self.maxTree(node.left)
        rres = self.maxTree(node.right)
        if res < lres:
            res = lres
        if res < rres:
            res = rres
        return res
    
    
    #min number
    def minTree(self,node):
        if node == None:
            return sys.maxsize
        res = node.data
        lres = self.minTree(node.left)
        if res > lres :
            res = lres
        rres = self.minTree(node.right)
        if res > rres :
            res = rres
            
        return res
    
    
    # left view of the tree
    def leftView(self):
        if self.root == None:
            return
        
        q1 = Queue()
        _left = []
        q1.push(self.root)
        while q1.emptyqueue() != 1:
            n = len(q1.queue)
            for i in range(n):
                temp = q1.pop()
                if i == 0:
                    #print(f"->{temp.data}",end=" ")
                    logging.info(f"->{temp.data}")
                    _left.append(temp.data)
                    if temp.left:
                        q1.push(temp.left)
                    if temp.right:
                        q1.push(temp.right)
        return _left
                        
                        
    # adding the right view of the tree
    def rightView(self):
        if self.root == None:
            return
        q1 = Queue()
        _right = []
        q1.push(self.root)
        while q1.emptyqueue() != 1:
            n = len(q1.queue)
            for i in range(n):
                temp = q1.pop()
                if i == 0:
                    #print(f"->{temp.data}",end=" ")
                    logging.info(f"->{temp.data}")
                    _right.append(temp.data)
                    if temp.right:
                        q1.push(temp.right)
                    if temp.left:
                        q1.push(temp.left)
        return _right
    
    
    #adding the top view the tree.
    def top_view(self):
        if self.root == None:
            return
        lview = self.leftView()
        rview = self.rightView()
        lview = lview[::-1]
        for i in rview:
            lview.append(i)
        lview = list(set(lview))
        for i in sorted(lview):
            print(i,end=" ")
            logging.info(i)
                
    # adding the bottom view of the tree
    def setHorizontalDistance(self,node,hd):
        if node is None:
            return
        self.setHorizontalDistance(node.left,hd-1)
        self.setHorizontalDistance(node.right,hd-1)
        
        
    def bottomView(self):
        if self.root is None:
            return
        self.setHorizontalDistance(self.root,0)
        # dictionary for storing the bottom view nodes
        bottom_view_map = {}
        q1 = Queue()
        q1.push(self.root)
        while q1.emptyqueue() != 1:
            node = q1.pop()
            hd = node.horizontal_distance
            
            bottom_view_map[hd] = node.data
            
            
            if node.left:
                q1.push(node.left)
                node.left.horizontal_distance = hd - 1
            
            if node.right:
                q1.push(node.right)
                node.right.horizontal_distance = hd - 1
                
        # print the bottom element
        for key in sorted(bottom_view_map):
            print(bottom_view_map[key],end=" ")
            logging.info(bottom_view_map[key])       
            
    # check sum property for tree
    def checkSum(self,node):
        if node == None:
            return True
        if node.left == None and node.right == None:
            return True
        sum = 0
        if node.left != None:
            sum += node.left.data
        if node.right != None:
            sum += node.right.data
        return node.data == sum and self.checkSum(node.left) and self.checkSum(node.right)
    
    # check the tree is balanced tree
    def checkBalance(self,node):
        if node is None:
            return 1
        lh = self.height(node.left)
        rh = self.height(node.right)
        
        if abs(lh - rh) <= 1 and self.checkBalance(node.left) and self.checkBalance(node.right):
            return 1
        return 0
        
    # get the max width for the tree
    def getWidth(self,node,level):
        if node == None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.getWidth(node.left,level-1) + self.getWidth(node.right,level-1)
        
        
    # function for getting the max width
    def getMaxWidth(self,node):
        try:
            maxWidth = 0
            h = self.height()
            for i in range(h):
                width = self.getWidth(node,i)
                if width > maxWidth:
                    maxWidth = width
                    
            return maxWidth
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
                
            
                    
        
        
        
        
    
        
        
        
        
root_data = int(input("enter the root for the data :"))
list1 = list(map(int,input("enter the all the tree data for the list (with comma):").split(",")))
t1 = Tree()
t1.insertTree(root_data)
for i in list1:
    t1.insertTree(i)

while True:
    print("\n1: insert \n2: delete \n3: search \n 0: exit")
    print("\n4: inorder traversal . \n5: postorder traversal \n6: preorder traversal")
    print("\n7: print from k th node. \n8: print the levelorder traversal.")
    print("\n9: size of the tree. \n10: max number of the tree .")
    print("\n11: min number of the tree. \n 12 : left view of the tree.")
    print("\n13: right view of the tree. \n14: top view of the tree.")
    print("\n15: bottom view tree. \n16: Check sum for tree.")
    print("\n17: check the tree is balanced.")
    print("\n18 : find the maxwidth of the tree.")
    choice = int(input("enter the choice :"))
    if choice == 0:
        exit(0)
    elif choice == 1:
        data = int(input("enter the data to the insert in the tree :"))
        t1.insertTree(data)
    elif choice == 2:
        data = int(input("enter the data to be delete :"))
        t1.deleteNode(data)
    elif choice == 3:
        data = int(input("enter the data to search :"))
        if t1.searchTree(t1.root,data) == False:
            print(f"{data} is not present in the tree.")
            logging.info(f"{data} is not present in the tree.")
        else:
            print(f"{data} is  present in the tree.")
            logging.info(f"{data} is present in the tree.")
            
    elif choice == 4:
        print("inorder traversal ----")
        logging.info("inorder traversal ----")
        t1.inorder_traversal()
    elif choice == 5:
        print("postorder traversal -----")
        logging.info("postorder traversall -----")
        t1.postorder()
    elif choice == 6:
        print("preorder traversal ---")
        logging.info("preorder traversal ---")
        t1.preOrder()
    elif choice == 7:
        data = int(input("enter the data from the where you want to  print :"))
        h1 = t1.height(t1.root)
        if data  < h1:
            t1.print_kth(data)
            
        else:
            print("can't perform op.")
            logging.error("can't perform.")
            
    elif choice == 8:
        print("\nlevel order traversal.")
        logging.info("level order traversal.")
        t1.levelOrder()
        
    elif choice == 9:
        data = t1.size(t1.root)
        print(f"the size of the tree is : {data}")
        logging.info(f"the size of the tree is : {data}")
        
    elif choice == 10:
        data = t1.maxTree(t1.root)
        print(f"the maximum number of the tree is : {data}")
        logging.info(f"the maximum number of the tree is : {data}")
        
    elif choice == 11:
        data = t1.minTree(t1.root)
        print(f"the minimum number of the tree is : {data}")
        logging.info(f"the minimum number of the tree is : {data}")
        
        
    elif choice == 12:
        print(f"left view of the tree.")
        logging.info(f"left view of the tree.")
        left = t1.leftView()
        print(left)
        logging.info(left)
        
        
    elif choice == 13:
        print("right view of the tree .")
        logging.info("right view of the tree.")
        print(t1.rightView())
        logging.info(t1.rightView())
        
        
    elif choice == 14:
        print("\nthe top view of the tree is :")
        logging.info("\nthe top view of the tree is :")
        t1.top_view()
        
        
        
    elif choice == 15:
        print("\nthe bottom view of the tree is:")
        logging.info("the bottom view of the tree is :")
        t1.bottomView()
        
        
    elif choice == 16:
        print("Checking the tree is check sum property :")
        logging.info("Checking the tree is check sum property :")
        if t1.checkSum(t1.root) == False:
            print("\nthe tree does not follow check sum.")
            logging.info("the tree does not follow check sum.")
        else:
            print("\nthe tree follows ")
            
    elif choice == 17:
        data = t1.checkBalance(t1.root)
        if data == 1:
            print("\nthe tree is balanced.")
            logging.info("the tree is balanced.")
        else:
            print("\nthe tree is not balanced.")
            logging.info("\nthe tree is not balanced.")
            
            
    elif choice == 18:
        data = t1.getMaxWidth(t1.root)
        
        print(f"The max width of the tree is : {data}")
        logging.info(f"The max width of the tree is : {data}")
    
        
