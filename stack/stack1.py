# implementing the stack for the linear data structure .


# set up log for the logger .
import sys
sys.path.append("D:/python_exercise_geeks/structer-1")

from settings import setup_logging
import logging

setup_logging()


class Stack:
    def __init__(self):
        self.stack = []
        
    # push operation for the stack
    def pushStack(self,data):
        if data:
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
            logging.info("{element} has been deleted.")
            
    
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
                print(f"\n{self.stack[i]}",end=" ")
            logging.info(self.stack)
                