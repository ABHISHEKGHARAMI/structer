# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()


'''
The Overlapping Dynamic programming
It Divides in two ways
i . Memorization (Top -down approach :) - with the example you can see the example of that
we store the value when it is needed.

ii. Tabulation (bottom - up approach :) - here we go storing from bottom level lookup table to upper - level 
setup .

'''
look_up = [0] * 100
def fibo(n):
    if look_up[n] == 0 :
        if n <= 1:
            look_up[n] = n
        else:
            look_up[n] = fibo(n-1) + fibo(n-2)
    return look_up[n]


# using the tabulation form
def fiboTab(n):
    look = [0]*(n+2)
    look[0] = 0
    look[1] = 1
    for i in range(2,n+1):
        look[i] = look[i-1] + look[i-2]
    return look[n]
    

# testing
n = int(input("enter the number to get the fibo :"))
print(f"The top -down approach of the fibo is : {fibo(n)}")
logging.info(f"The top -down approach of the fibo is : {fibo(n)}")

print(f"The fibo of the {n} is : {fiboTab(n)}")
logging.info(f"the fibo of the {n} is : {fiboTab(n)}")

