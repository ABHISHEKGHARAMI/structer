'''
You are given an array A of size N. 
You need to first push the elements of the array into a stack and then print minimum 
in the stack at each pop until stack becomes empty.

Example 1:

Input:
N = 5
A = {1 2 3 4 5}
Output: 
1 1 1 1 1
'''

# setting up the logger

import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()

# stack implementation


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
    
    
    # function for returning the lowest value for the stack
    def lowestvalue(self):
        if len(self.stack) == 0:
            return -1
        else:
            return min(self.stack)

# function for the min pop operation
def popMin(arr):
    try:
        s1 = Stack()
        for i in arr:
            s1.pushStack(i)
        temp = []
        while not s1.isEmpty():
            if s1.topStack() >= s1.lowestvalue():
                temp.append(s1.lowestvalue())
                s1.stack.pop()
        return temp
    except Exception as e:
        print(e)
        logging.info(e)
        
        
# execution for the function
arr = [1, 6, 43, 1, 2, 0, 5]
print(f"After pop min operation for the array is : {popMin(arr)}")