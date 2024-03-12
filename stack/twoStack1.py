'''

The idea to implement two stacks is to divide the array into two halves and assign 
two halves to two stacks, i.e., use arr[0] to arr[n/2] for stack1, 
and arr[(n/2) + 1] to arr[n-1] for stack2 where arr[] is the array to be used to 
implement two stacks and size of array be n. 

'''

# set up the logger file


from math import floor
import logging
from settings import setup_logging
import sys
sys.path.append("D:/python_exercise_geeks/structer-1")


setup_logging()


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

    # pop the middle element
    def middlePop(self):
        if self.isEmpty() == 1:
            print("\nthe Stack is empty.")
            logging.error("Stack is empty.")
        else:
            size = self.sizeStack()
            data = self.stack.pop(floor(size//2))
            print(f"{data} deleted form the stack.")
            logging.info(f"{data} deleted form the stack.")
            
            
s1 = Stack()
s2 = Stack()


arr = [1,2,3,5,6,6,7,8,9,10]

if len(arr) == 0:
    print("\nThe array is empty.")
    logging.info("The array is empty.")
else:
    size = len(arr)
    for i in range(size//2):
        s1.pushStack(arr[i])
    for i in range(size//2+1,size):
        s2.pushStack(arr[i])
        
    # print the two stack
    s1.printStack()
    s2.printStack()
    m , n = map(int,input("\nEnter the two input for two stack :").split(","))
    s1.pushStack(m)
    s2.pushStack(n)
    # print the stack
    s1.printStack()
    s2.printStack()
    
    # pop the stack
    s1.popStack()
    s2.popStack()
