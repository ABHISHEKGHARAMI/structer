'''
Find the largest rectangular area possible in a given histogram where the largest 
rectangle can be made of a number of contiguous bars whose heights are given in an array. 
For simplicity, assume that all bars have the same width and the width is 1 unit. 
'''

# setting up the logger file




import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


setup_logging()

# setting for stack class


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
        
        
#  function for the largest histogram 
def largestHistogramArea(height):
    try:
        s1 = Stack()
        index = 0
        maxArea = 0
        while index < len(height)-1:
            if not s1 or height[index] >=  height[s1.stack[-1]]:
                s1.pushStack(index)
                index += 1
            else:
                top_of_stack = s1.stack.pop()
                width = index if not s1 else index - s1.stack[-1] - 1
                top_of_area = width * height[top_of_area]
                maxArea = max(maxArea,top_of_area)
        
        while s1:
            top_of_stack = s1.stack.pop()
            width = index if not s1 else index - s1.stack[-1] - 1
            top_of_area = width * height[top_of_stack]
            maxArea = max(top_of_area,maxArea)
        return maxArea
    except Exception as e:
        print(e)
        logging.info(e)
        
        
        
# execution for the largest histogram 
height = [6, 2, 5, 4, 5, 1, 6]
area = largestHistogramArea(height)
print(f"the max area of the histogram is : {area}")
logging.info(f"the max area of the histogram is : {area}")
