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
    
    
"""

here we go for the dynamic aproach of the program for the fibonacci series
in this algorithm we need to store the previous result.
"""


def fibo_Dynamic(num):
    fibo = [0] * (num+2)
    fibo[0] = 0
    fibo[1] = 1
    
    for i in range(2,len(fibo)):
        fibo[i] = fibo[i-1] + fibo[i-2]
        
    return fibo[num]
    
num = int(input("enter the number to get the fibonnaci :"))

print(f"the fibonacci addition of the {num} is : {fibo_recurr(num)}")
logging.info("the fibonacci addition of the {num} is : {fibo_recurr(num)}")


print(f"After the dynamic approach the result will be : {fibo_Dynamic(num)}")
logging.info(
    f"After the dynamic approach the result will be : {fibo_Dynamic(num)}")


