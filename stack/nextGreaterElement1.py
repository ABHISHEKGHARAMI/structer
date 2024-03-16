'''

Given an array, print the Next Greater Element (NGE) for every element. 

The Next greater Element for an element x is the first greater element on the right side
of x in the array. Elements for which no greater element exist, consider the next greater element as -1.
 
'''

# setting up the logger file

import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


# class for the next greater element
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


# function for the next greater element
def nextGreater(arr):
    try:
        s1 = Stack()
        temp = []
        n = len(arr) 
        i = 0
        while i < n - 1:
            if arr[i] < arr[i+1]:
                s1.pushStack(arr[i+1])
            else:
                j = i + 1
                while j < n:
                    if arr[i] < arr[j]:
                        s1.pushStack(arr[j])
                    j+=1
            i+=1
            temp = []
            for i in range(s1.sizeStack()):
                temp.append(s1.stack.pop())
            temp = temp[::-1]
            temp[-1] = -1
            return temp 
                            
    except Exception as e:
        print(e)
        logging.info(e)
        
        
# main execution of the program
arr = [4,5,2,25]

print(f"The next greater element array by the operation will be : {nextGreater(arr)}")
logging.info(f"The next greater element array by the operation will be : {nextGreater(arr)}")