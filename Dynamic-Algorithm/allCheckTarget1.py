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


targetString = "abcdef"
charArray = ['ab', 'abc', 'cd', 'def', 'abcd']


print(f"All the possible output will be : {recursive(targetString,charArray)}")
