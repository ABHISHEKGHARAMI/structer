# problem statement
'''
The stock span problem is a financial problem where we have a series of N 
daily price quotes for a stock and we need to calculate the span of the stock's price 
for all N days. The span Si of the stock's price on a given day i is defined 
as the maximum number of consecutive days just before the given day, 
for which the price of the stock on the current day is less than its price on the given day. 

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

#function for the span of the function
def spanStock(prices):
    try:
        n = len(prices)
        stack = Stack()
        span = [0] * n
        stack.pushStack(0)
        span[0] = 1
        for i in range(1,n):
            while  not stack.isEmpty() and prices[stack.topStack()] <= prices[i]:
                stack.popStack()
            span[i] = i + 1 if stack.isEmpty() else (i - stack.topStack())
            stack.pushStack(i)
        return span
    except Exception as e:
        print(e)
        logging.info(e)
        
        
# executing the main function
prices = [100,80,60,70,60,75,85]
print(spanStock(prices))
logging.info(spanStock(prices))
