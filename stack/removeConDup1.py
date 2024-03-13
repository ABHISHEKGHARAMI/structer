# setting up the logger

import sys
sys.path.append("D:/python_exercise_geeks/structer-1")

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
        
    # function for value containing
    def __contain__(self,data):
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
        
# function for removing the cons duplicate from the string
def removeDuplicate(exp):
    try:
        s1 = Stack()
        if exp is None:
            print("\nNo expression given")
            logging.error("No expression given.")
            
            return ""
        else:
            for x in exp:
                if s1.topStack() == x:
                    continue
                else:
                    s1.pushStack()
            # have to print the stack for the string
            str1 = ""
            for i in self.stack:
                str1+=i
            return str1
                
            
        
    except Exception as e:
        print(e)
        logging.error(e)

exp = "aaaaaaabaabccccccc"
print(f"After removing the consequtive duplicate from the string will be : {removeDuplicate(exp)}")
logging.info(
    f"After removing the consequtive duplicate from the string will be : {removeDuplicate(exp)}")

