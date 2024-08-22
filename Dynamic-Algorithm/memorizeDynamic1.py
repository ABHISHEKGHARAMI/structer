# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging
setup_logging()



"""
In memorize approach we need to set up a look up table for the data to be precomputed  or at-least  check it for
further approach .
"""
def intialize(num):
    fb = [0] * 100
    return fiboMemorize(num,fb)
    
    
def fiboMemorize(num,fb):
    if fb[num] == 0:
        if num <= 1:
            return num
        else:
            fb[num] = fiboMemorize(num-1,fb) + fiboMemorize(num-2,fb)
            
    return fb[num]


#  input

num = int(input("enter the number as a input :"))

print(f"The {num} of fibonacci is : {intialize(num)}")