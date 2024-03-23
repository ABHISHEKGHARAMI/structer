#  infix to postfix expression

# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()


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

# order of the operator
def order(x):
    if x == '^':
        return 3
    elif x == '/' or x == '*':
        return 2
    elif x == '+' or x == '-':
        return 1
    else:
        return -1
    
# function for the infix to postfix expression
def infix_postfix(exp):
    try:
        s1 = Stack()
        result = ""
        for i in range(len(exp)):
            # first check if it is operand
            if exp[i] >='a' and exp[i] <='z' or exp[i] >='A' and exp[i] <='Z' :
                result+=exp[i]
            # check if the '(' then push it to the stack
            elif exp[i] =='(':
                s1.pushStack(exp[i])
            # check if the ')' then pop until '(' appears
            elif exp[i] ==')':
                while s1.topStack() !='(':
                    result += s1.topStack()
                    s1.stack.pop()
                s1.stack.pop()
            # if the operator is scanned
            else:
                while s1.isEmpty() != 1 and  order(exp[i]) <= order(s1.topStack()):
                    result += s1.topStack()
                    s1.stack.pop()
                s1.pushStack(exp[i])
            
            # empty the stack
        while s1.isEmpty() != 1:
            result += s1.stack.pop()
            
        return result
                    
    except Exception as e:
        print(e)
        logging.error(e)
        
        
# execution for the infix to postfix expression
exp = str(input("Enter the expression :"))

result = infix_postfix(exp)

print(f"The infix expression to postfix expression of {exp} will be : {result}")
logging.info(f"The infix expression to postfix expression of {exp} will be : {result}")