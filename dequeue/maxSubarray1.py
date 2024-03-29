'''
Given an array and an integer K, find the maximum for each and every contiguous subarray of size K.

Examples : 

Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3 
Output: 3 3 4 5 5 5 6
Explanation: Maximum of 1, 2, 3 is 3
                       Maximum of 2, 3, 1 is 3
                       Maximum of 3, 1, 4 is 4
                       Maximum of 1, 4, 5 is 5
                       Maximum of 4, 5, 2 is 5 
                       Maximum of 5, 2, 3 is 5
                       Maximum of 2, 3, 6 is 6

Input: arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}, 

'''
# set up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging


setup_logging()
from collections import deque

def maxSubarray(q,k):
    max_list = []
    for i in range(len(q)-k + 1):
        max_list.append(max(q[i:i+k]))
        
    print(f"The maximum sub array of the given array : {max_list}")
    logging.info(f"The maximum sub array of the given array : {max_list}")
    
    
# execution of the program
q = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
maxSubarray(q,3)
    