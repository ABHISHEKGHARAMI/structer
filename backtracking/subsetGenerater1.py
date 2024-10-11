'''
Given an array of integers arr[], The task is to find all its subsets. 
The subset can not contain duplicate elements, so any repeated subset 
should be considered only once in the output.

Examples: 

Input:  S = {1, 2, 2}
Output:  {}, {1}, {2}, {1, 2}, {2, 2}, {1, 2, 2}
Explanation: The total subsets of given set are – {}, {1}, {2}, {2}, {1, 2}, {1, 2}, {2, 2}, {1, 2, 2}
Here {2} and {1, 2} are repeated twice so they are considered only once in the output



Input:  S = {1, 2}
Output:  {}, {1}, {2}, {1, 2}
Explanation: The total subsets of given set are – {}, {1}, {2}, {1, 2}
'''

# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()

# bit masking approach using brute force approach
def find_subset(ind,nums,ds,any_list):
    any_list.append(list(ds))
    for i in range(ind,len(nums)):
        if i != ind and nums[i] == nums[i-1]:
            continue
        ds.append(nums[i])
        find_subset(ind+1,nums,ds,any_list)
        ds.pop()

# main function
def all_subset(arr):
    ind = 0
    nums = sorted(arr)
    ds = []
    any_list = []
    find_subset(ind,nums,ds,any_list)
    return any_list


# testing the result
subset = all_subset([5,4,1,2,3])

for item in subset:
    print(f"{item}",end=",")
logging.info(f"{subset}")