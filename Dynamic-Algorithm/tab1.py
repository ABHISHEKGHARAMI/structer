# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging
setup_logging()

# fib with tabular solution


def fib(num):
    f = [0] * (num+2)
    f[0] = 0
    f[1] = 1
    for i in range(2,num+2):
        f[i] = f[i-1] + f[i-2]
        
    return f[num]

num = 5
print(f"the fib of {num} is : {fib(num)}")
logging.info(f"the fib of {num} is : {fib(num)}")
