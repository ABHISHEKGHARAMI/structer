# setting up  the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()


'''
Problem statement : An target string and an char array is given task is to find the all the combination
of the possible solution in 2D array
'''

def recursive(targetString,charArray):
    if targetString == "":
        return [[]]
    
    result = []
    
    for char in charArray:
        if targetString.startswith(char):
            remainder = targetString[len(char):]
            if recursive(remainder,charArray):
                result_remainder = recursive(remainder,charArray)
                
                for ways in result_remainder:
                    result.append([char]+ways)
    return result


# using the dyanmic approach
def dynamic(targetString,charArray,memo=None):
    if memo is None:
        memo = {}
        
    if targetString in memo:
        return memo[targetString]
    
    if targetString == "":
        return [[]]
    
    result = []
    
    for char in charArray:
        if targetString.startswith(char):
            remainder = targetString[len(char):]
            if dynamic(remainder,charArray):
                result_remainder = dynamic(remainder,charArray)
                
                for ways in result_remainder:
                    result.append([char]+ways)
                    
    memo[targetString] = result
    return memo[targetString]


targetString = "abcdef"
charArray = ['ab', 'abc', 'cd', 'def', 'abcd']


print(f"All the possible output of the target string {targetString} will be : {recursive(targetString,charArray)}")
logging.info(f"All the possible output of the target string {targetString} will be : {recursive(targetString,charArray)}")
