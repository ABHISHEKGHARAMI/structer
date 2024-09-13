# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()


'''
Problem Statement :
   An array of the elements and a target  sum is given task is to find the shortest for the combination for that.
   in put : (2,3,4,7),7 output will be [7]
 '''
 
def shortestComb(array,targetSum):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    shortest = None
    for num in array:
        remainder = targetSum - num
        remResult = shortestComb(array,remainder)
        if remResult != None:
            combination = remResult + [num]
            if shortest is None or len(combination) < len(shortest):
                shortest = combination
                
    return shortest


# Dynamic solution of the program
def shortestDynamic(array,targetSum,memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    shortest = None
    
    for num in array:
        remainder = targetSum - num
        remResult = shortestDynamic(array,remainder)
        if remResult != None:
            combination = remResult + [num]
            if shortest  is None or len(combination) < len(shortest):
                shortest = combination
                
    memo[targetSum] = shortest
    return memo[targetSum]

# checking the program
arr = [5,3,4,7]
target = 7

print(f'the shortest combination is : {shortestComb(arr,target)}')
logging.info(f'the shortest combination is : {shortestComb(arr,target)}')
                
print(f'the shortest combination is : {shortestComb([2,3,5],8)}')
logging.info(f'the shortest combination is : {shortestComb([2,3,5],8)}')


# testing the dynamic solution
print(f'the shortest combination is : {shortestDynamic(arr,target)}')
logging.info(f'the shortest combination is : {shortestDynamic(arr,target)}')

print(f'the shortest combination is : {shortestDynamic([2,3,5],8)}')
logging.info(f'the shortest combination is : {shortestDynamic([2, 3, 5],8)}')
