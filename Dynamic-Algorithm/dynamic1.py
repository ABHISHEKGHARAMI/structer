# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging
setup_logging()


# using the recursion for the fibonacci result
def fibo_recurr(num):
    if num <= 1:
        return num
    else:
        return fibo_recurr(num-1) + fibo_recurr(num-2)
    
    
num = int(input("enter the number to get the fibonnaci :"))

print(f"the fibonacci addition of the {num} is : {fibo_recurr(num)}")
logging.info("the fibonacci addition of the {num} is : {fibo_recurr(num)}")
