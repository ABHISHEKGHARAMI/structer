# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()

'''
problem statement an array and a number is given find the solution to check that 
array consist the sum of the data in the list.
'''

# recursion 
def checkSumRecurr(array,targetSum) :
    if targetSum == 0:
        return True
    if len(array) == 0:
        return False
    # case 1 : check the element is greater than the element then ignore it.
    if array[-1] > targetSum:
        checkSumRecurr(array[:-1],targetSum)
    # case 2 : check the two possibility
    # a : include it the checksum
    # b : exclude it from the checksum
    return checkSumRecurr(array[:-1],targetSum-array[-1]) or checkSumRecurr(array[:-1],targetSum)


array = list(map(int,input("enter the elements :").split(',')))
target = int(input("enter the target:"))

if checkSumRecurr(array,target) == True:
    print(f"{target} can be acheived using the array.")
    logging.info(f"{target} can be acheived using the array.")
else:
    print(f"{target} can not be acheived using the array.")
    logging.info(f"{target} can not be acheived using the array.")
