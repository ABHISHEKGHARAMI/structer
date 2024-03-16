'''
Given an array of distinct elements, find previous greater element for every element.
If previous greater element does not exist, print -1.

Examples: 

Input : arr[] = {10, 4, 2, 20, 40, 12, 30}
Output :         -1, 10, 4, -1, -1, 40, 40

Input : arr[] = {10, 20, 30, 40}
Output :        -1, -1, -1, -1

Input : arr[] = {40, 30, 20, 10}
Output :        -1, 40, 30, 20
Expected time complexity : O(n)

'''

# setting up the logger file

import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


# class for stack


class Stack:
    def __init__(self):
        self.stack = []

    # push operation for the stack
    def pushStack(self, data):
        if data is None:
            print(f"\nData is empty.")
            logging.error("Data is empty.")
        else:
            print(f"Inserting the {data}")
            logging.info(f"Inserting the {data}")
            self.stack.append(data)

    # isEmpty for the stack

    def isEmpty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0

    # pop for the stack
    def popStack(self):
        if self.isEmpty() == 1:
            print("\nThe stack is empty.")
            logging.error("Stack is empty.")
        else:
            element = self.stack.pop()
            print(f"{element} has been pop from the stack.")
            logging.info(f"{element} has been deleted.")

    # size of the stack

    def sizeStack(self):
        if self.isEmpty() == 1:
            return 0
        else:
            return len(self.stack)

    # print the stack
    def printStack(self):
        if self.isEmpty():
            print("\nThe stack is empty.")
        else:
            for i in range(len(self.stack)):
                print(f"\n{self.stack[i]}", end=" ")
            logging.info(self.stack)

    # top of the element of the stack

    def topStack(self):
        if self.isEmpty() == 1:
            return 0
        else:
            return self.stack[-1]

    # function for value containing
    def __contain__(self, data):
        if data is None:
            return 0
        else:
            flag = 0
            for i in range(len(self.stack)):
                if self.stack[i] == data:
                    flag = 1
                    break
            if flag == 1:
                return 1
            return 0
    
    
# function for the stack the previous greater element

def frontGreater(arr):
    try:
        s1 = Stack()
        s1.pushStack(-1)
        for i in range(1,len(arr)-1):
            if arr[i-1] > arr[i]:
                s1.pushStack(arr[i-1])
            else:
                s1.pushStack(-1)
        temp = []
        for i in range(s1.sizeStack()):
            temp.append(s1.stack.pop())
        temp = temp[::-1]
        return temp
    except Exception as e:
        print(e)
        logging.info(e)
        
        


# execution for the stack
arr = [10, 4, 2, 20, 40, 12, 30]

temp = frontGreater(arr)


print(f"After the operation the stack will be : {temp}")
logging.info(f"After the operation the next greater element will be : {temp}")