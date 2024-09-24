# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()


'''
Problem statement : The target string , and an array of the char is given then find the boolean from the array
of the char to from the target string.
'''

def can_target_string(targetString,charArray):
    if targetString == '':
        return True
    
    for char in charArray:
        if targetString.startswith(char):
            remiander = targetString[len(char):]
            
            if can_target_string(remiander,charArray):
                return True
            
    return False


targetString = "abcdef"
charArray = ['ab','abc','cd','def','abcd']


if can_target_string(targetString,charArray) == True:
    print(f"The {targetString} can be build using the charArray.")
    logging.info(f"The {targetString} can be build using the charArray.")
else:
    print(f"The {charArray} can not build from the charArray.")
    logging.info(f"The {charArray} can not build from the charArray.")
