# setting up  the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()


'''
Problem statement : The target string , and an array of the char is given then find the number of ways to
construct the string from the array
of the char to from the target string.
'''

# recursive solution
def count_target_construct(targetString,charArray):
    if targetString == "":
        return 1
    count = 0 
    for char in charArray:
        if targetString.startswith(char):
            remainder = targetString[len(char):]
            if count_target_construct(remainder,charArray):
                count += count_target_construct(remainder,charArray)
    return count


# the dynamic approach
def count_target_dynamic(targetString,charArray,memo=None):
    if memo is None:
        memo = {}
        
    if targetString in memo:
        return memo[targetString] 
    
    if targetString == "":
        return 1
    
    count = 0 
    
    for char in charArray:
        if targetString.startswith(char):
            remainder = targetString[len(char):]
            if count_target_dynamic(remainder,charArray):
                count += count_target_dynamic(remainder,charArray)
                
    # finally update the memory
    memo[targetString] = count
    return memo[targetString]
    
    

targetString = "abcdef"
charArray = ['ab', 'abc', 'cd', 'def', 'abcd']

print(f"the number is : {count_target_construct(targetString,charArray)}")
logging.info(f"the number is : {count_target_construct(targetString,charArray)}")

print(f"the number is : {count_target_dynamic(targetString,charArray)}")
logging.info(f"the number is : {count_target_dynamic(targetString,charArray)}")
