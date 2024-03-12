'''
Given a stack, delete the middle element of the stack without using any additional data structure.
Middle element:- floor((size_of_stack+1)/2) (1-based indexing) from bottom of the stack.
'''
import sys
sys.path.append("D:/python_exercise_geeks/structer-1")

from settings import setup_logging
import logging

setup_logging()
from math import floor


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
            logging.info("Inserting the {data}")
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
        
    #pop the middle element
    def middlePop(self):
        if self.isEmpty() == 1:
            print("\nthe Stack is empty.")
            logging.error("Stack is empty.")
        else:
            size = self.sizeStack()
            data = self.stack.pop(floor(size//2))
            print(f"{data} deleted form the stack.")
            logging.info(f"{data} deleted form the stack.")
            


# executing the stack for the

s1 = Stack()
s1.pushStack(10)
s1.pushStack(20)
s1.pushStack(30)
s1.pushStack(40)
s1.pushStack(50)
s1.pushStack(60)
s1.middlePop()
