'''
Given an expression string exp, write a program to examine whether the pairs and 
the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression.'''




import sys
sys.path.append("D:/python_exercise_geeks/structer-1")

from settings import setup_logging
import logging

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


# function for check parenthesis
def checkParenthesis(exp):
    bracket = ['(','[','{']
    s1 = Stack()
    flag = 0
    for str1 in exp:
        if str1 in bracket:
            s1.pushStack(str1)
        elif str1 in [')',']','}']:
            if s1.isEmpty() == 1 or not  matching(s1.topStack(),str1):
                return 0
            else:
                s1.popStack()
        else:
            continue
    if s1.isEmpty() == 1:
        return 1
    else:
        return 0
    
# for matching
def matching(char1 , char2):
    if char1 == '(' and char2 ==')':
        return True
    if char1 == '{' and char2 == '}':
        return True
    if char1 == '[' and char2 == ']':
        return True
    return False
        

# execute the main function
exp = str(input("enter any expression with parenthesis :"))

if checkParenthesis(exp) == 1:
    print(f"{exp} has balanced parenthesis :")
    logging.info(f"{exp} has balanced parenthesis .")
else:
    print(f"{exp} is not balanced at all.")
    logging.info(f"{exp} is not balanced at all .")
