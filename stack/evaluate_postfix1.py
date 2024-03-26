#Evaluate the postfix expression

# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()

# class for the stack
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
        
# evaluate the function
def evaluate(exp):
    try:
        s1 = Stack()
        for i in exp:
            if i.isdigit():
                s1.pushStack(int(i))
            else:
                op2 = s1.stack.pop()
                op1 = s1.stack.pop()
                if i == '+':
                    s1.pushStack(op1 + op2)
                elif i == '-':
                    s1.pushStack(op1 - op2)
                elif i =='*':
                    s1.pushStack(op1 * op2)
                elif i == '/':
                    s1.pushStack(op1 / op2)
        return s1.stack.pop()
    except Exception as e:
        print(e)
        logging.error(e)
        
        
# execution for the eval
exp = str(input("Enter the expression :"))
result = evaluate(exp)

print(f"After evaluating the expression {exp} is : {result}")
logging.info(f"After evaluating the expression {exp} is : {result}")
