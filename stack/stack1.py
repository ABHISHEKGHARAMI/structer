# implementing the stack for the linear data structure .


# set up log for the logger .
import sys
sys.path.append("D:/geeks1.0/structer")

from settings import setup_logging
import logging

setup_logging()


class Stack:
    def __init__(self):
        self.stack = []
        
    # push operation for the stack
    def pushStack(self,data):
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
                print(f"\n{self.stack[i]}",end=" ")
            logging.info(self.stack)
            
            
    # top of the element of the stack
    def topStack(self):
        if self.isEmpty() == 1:
            return 0
        else:
            return self.stack[-1]


# executing the stack for the 

s1 = Stack()

# loop
while True  :
    print("\n 1: Append data. \n 2: Pop Data. \n 3: Size of Stack. \n 4: Print Stack.")
    print("\n 5. Print the top of the element \n0: exit the program.")
    choice = int(input("\nenter the choice :"))
    if choice == 0:
        exit(0)
    elif choice == 1:
        data = int(input("\nEnter the data to Push in the stack."))
        s1.pushStack(data)
    elif choice == 2:
        s1.popStack()
    elif choice == 3:
        print(f"\nthe size of the stack is : {s1.sizeStack()}")
        logging.info(f"the size of the stack is : {s1.sizeStack()}")
    elif choice == 4:
        s1.printStack()
    elif choice == 5:
        if s1.topStack() == 0:
            print("\nStack empty.")
        else:
            print(f"The top of the element is : {s1.topStack()}")
    else:
        print("Wrong choice !!")
        logging.info("Wrong choice !!")
        # adding coment to see is git working or not.