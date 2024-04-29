# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


class Queue:
    def __init__(self):
        self.queue = []
        
    def push(self,data):
        self.queue.append(data)
        
    def pop(self):
        if self.isEmpty() == 1:
            print("Queue is under flowed.")
            logging.info("Queue is under flowed.")
            return -1
        else:
            return self.queue.pop(0)
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
        
    def front(self):
        if self.isEmpty() == 1:
            return -1
        else:
            return self.queue[0]

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.root = None
        
        
    # insertion in tree
    def insertion(self,data):
        print(f"inserting {data} in the tree.")
        logging.info(f"inserting {data} in the tree.")
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.insert_recursive(self.root,data)
            
    # insertion of the tree
    def insert_recursive(self,node,data):
        try:
            if node.data < data:
                if not node.right :
                    node.right = TreeNode(data)
                else:
                    self.insert_recursive(node.right,data)
            elif node.data > data:
                if not node.left :
                    node.left = TreeNode(data)
                else:
                    self.insert_recursive(node.left,data)
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
        
    # height of the tree
    def height(self,node):
        try:
            if node == None:
                return 0
            else:
                lheight = self.height(node.left)
                rheight = self.height(node.right)
                return max(lheight,rheight) + 1
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
        
        
        
    # find the min of the tree
    def find_min(self,node):
        try:
            if not node:
                return
            else:
                while node.left:
                    node = node.left
                return node.data
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
        
        
    # delete the node
    def delete(self,data):
        print(f"deleting the {data} from the tree.")
        logging.info(f"deleting the {data} from the tree.")
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
            logging.info(e)
            raise Exception
        
        
    # search the tree
    def searchTree(self,node,data):
        if node == None:
            return False
        else:
            if node.data == data:
                return True
            elif node.data < data:
                return self.searchTree(node.right,data)
            else:
                return self.searchTree(node.left,data)
            
    
    
    # traversal of the tree
    def inOrder(self):
        if self.root:
            self.inOrder_recurr(self.root)
            
    def inOrder_recurr(self,node):
        if node:
            self.inOrder_recurr(node.left)
            print(f"->{node.data}",end=" ")
            logging.info(f"->{node.data}")
            self.inOrder_recurr(node.right)
            
            
    # pre order and post order recurr
    def preOrder(self):
        if self.root:
            self.preOrder_recurr(self.root)
            
    def preOrder_recurr(self,node):
        if node:
            print(f"->{node.data}",end=" ")
            logging.info(f"->{node.data}")
            self.preOrder_recurr(node.left)
            self.preOrder_recurr(node.right)
            
            
    def postOrder(self):
        if self.root:
            self.postorder_recur(self.root)
            
    def postorder_recur(self,node):
        if node:
            self.postorder_recur(node.left)
            self.postorder_recur(node.right)
            print(f"->{node.data}",end=" ")
            logging.info(f"->{node.data}")
            
            
    # size of the tree
    def sizetree(self,node):
        try:
            if node == None:
                return 0
            else:
                return self.sizetree(node.left) + 1 + self.sizetree(node.right)
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
            
            
    
    # print the kth data
    def print_kth(self,k):
        try:
            self.print_kth_recurr(self.root,k)
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
        
    
    def print_kth_recurr(self,node,k):
        try:
            if node is None or k < 0:
                return
            
            if k == 0:
                print(f"->{node.data}",end = " ")
                logging.info(f"->{node.data}")
            self.print_kth_recurr(node.left,k-1)
            self.print_kth_recurr(node.right,k-1)
            
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
        
        
    # max element of the tree
    def maxBST(self,node):
        try:
            if node is None:
                return -sys.maxsize
            res = node.data
            lres = self.maxBST(node.left)
            if lres > res:
                res = lres
            rres = self.maxBST(node.right)
            if rres > res :
                res = rres
            return res
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
        
        
    # min Element of the BST
    def minBST(self,node):
        try:
            if node is None:
                return sys.maxsize
            res = node.data
            lres = self.minBST(node.left)
            if lres < res :
                res = lres
            rres = self.minBST(node.right)
            if rres < res:
                res = rres
            return res
        except Exception as e:
            print(e)
            logging.info(e)
            raise Exception
            
            
            
    # level order traversal for the BST
    def levelOrder(self):
        if self.root is None:
            return
        q1 = Queue()
        q1.push(self.root)
        while q1.isEmpty() != 1:
            node_queue = q1.queue[0]
            print(f"->{node_queue.data}",end=" ")
            logging.info(f"->{node_queue.data}")
            q1.pop()
            
            if node_queue.left:
                q1.push(node_queue.left)
            
            if node_queue.right:
                q1.push(node_queue.right)
            
        
        
t1 = Tree()      
while True:
    print("\n0: exit program. \t1: insert. \t2: height. \t3: find min. \t4: delete. \t5: search.")
    print("\n6: Inorder. \t7: preorder \t8: postorder. \t9: size of tree. \t10: print kth node.")
    print("\n11 : max element. \t12: min element. \t13: level order traversal.")
    choice = int(input("\nenter the choice :"))
    if choice == 1 :
        data = int(input("enter the data to be insert :"))
        t1.insertion(data)
        
    elif choice == 2:
        h1 = t1.height(t1.root)
        print(f"the height of the tree is : {h1}")
        logging.info(f"the height of the tree is : {h1}")
        
        
    elif choice == 3:
        print(f"the min element of the tree is : {t1.find_min(t1.root)}")
        logging.info(f"the min element of the tree is : {t1.find_min(t1.root)}")
        
        
    elif choice == 4:
        data = int(input("enter the data for delete :"))
        t1.delete(data)
        
    elif choice == 5:
        data = int(input("\nenter the data to be search :"))
        flag = t1.searchTree(t1.root,data)
        if flag == True:
            print(f"{data} is present in the tree.")
            logging.info(f"{data} is present in the tree.")
        else:
            print(f"{data} not present in the tree.")
            logging.info(f"{data} is not present in the tree.")
            
    elif choice == 6:
        print("\ninorder traversal.")
        logging.info("inorder traversal.")
        t1.inOrder()
        
        
    elif choice == 7:
        print("\npreorder tranversal")
        logging.info("\nPreorder traversal :")
        t1.preOrder()
        
    elif choice == 8:
        print("\nPostorder traversal.")
        logging.info("\nPostorder traversal.")
        t1.postOrder()
        
        
    elif choice == 9:
        size = t1.sizetree(t1.root)
        print(f"the size of the binary search tree is : {size}")
        logging.info(f"the size of the binary search tree is : {size}")
        
    elif choice == 0:
        exit(0)
        
        
    elif choice == 10:
        k = int(input("enter the data from where to print:"))
        t1.print_kth(k)
        
        
    elif choice == 11:
        max_ele = t1.maxBST(t1.root)
        print(f"the max element in the bst is : {max_ele}")
        logging.info(f"the max element in the bst is : {max_ele}")
        
        
    elif choice == 12:
        min_ele = t1.minBST(t1.root)
        print(f"the min element of the bst is : {min_ele}")
        logging.info(f"the min element of the bst is : {min_ele}")
        
        
    elif choice == 13:
        print("level order traversal:")
        logging.info("level order traversal :")
        t1.levelOrder()
