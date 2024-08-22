# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging
setup_logging()


'''
for tabular algorithm we approach we start from the top

'''

def fibotabDynamic(num):
    fib = [0] * (num+2)
    fib[0] = 0
    fib[1] = 1
    for i in range(2,num+1):
        fib[i] = fib[i-1] + fib[i-2]
        
    return fib[num]


# input

num = int(input("enter the number as a input :"))

print(f"After the tabular method {num} is : {fibotabDynamic(num)}")
logging.info(f"After the tabular method {num} is : {fibotabDynamic(num)}")
