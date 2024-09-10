# setting up the logger 
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()

'''
Problem Statement : This time a number array and a target sum is given return any list which
consist of the sum of the element given the target.
'''
def recurHowSum(array,target) : 
    if target == 0:
        return []
    if target < 0:
        return None
    
    for num in array:
        remainder = target - num
        remResult = recurHowSum(array,remainder)
        if remResult != None:
            return [remainder,num]
    return None



# using the dynamic memorization approach
def howSumDynamic(array,target,memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for num in array:
        remainder = target - num
        remResult = howSumDynamic(array,remainder,memo)
        if remResult != None:
            memo[target] = [remainder,num]
            
    return None


arr = [4,5,2,1]
target = 9

print(f"the combination is : {recurHowSum(arr,target)}")
logging.info(f"the combination is : {recurHowSum(arr,target)}")

print(f"the combination using the dynamic approach  is : {howSumDynamic(arr,target)}")
logging.info(f"the combination using the dynamic approach is : {howSumDynamic(arr,target)}")
