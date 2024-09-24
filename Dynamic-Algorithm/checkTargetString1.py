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


# making the dynamic solution
def check_target_dynmic(targetString,charArray):
    dp = [False]*(len(targetString)+1)
    dp[0] = True
    
    # iterative over the string
    for i in range(len(targetString)):
        # it prefix can not form
        if dp[i]:
            # check that target string starts 
            for char in charArray:
                if targetString[i:i+len(char)] == char:
                    if  i + len(char) <= len(targetString):
                        dp[i+len(char)] = True
                        
    return dp[len(targetString)]

targetString = "abcdef"
charArray = ['ab','abc','cd','def','abcd']


if can_target_string(targetString,charArray) == True:
    print(f"The {targetString} can be build using the charArray.")
    logging.info(f"The {targetString} can be build using the charArray.")
else:
    print(f"The {charArray} can not build from the charArray.")
    logging.info(f"The {charArray} can not build from the charArray.")
    
    
#
if check_target_dynmic(targetString,charArray) == True:
    print(f"The {targetString} can be build using the charArray.")
    logging.info(f"The {targetString} can be build using the charArray.")
else:
    print(f"The {charArray} can not build.")
    logging.info(f"The {charArray} can not build.")
