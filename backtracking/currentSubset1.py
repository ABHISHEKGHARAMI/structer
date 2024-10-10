'''
Problem Statement :
Given an array Arr[] of size N, print all the subsets of the array.

Subset: A subset of an array is a tuple that can be obtained 
from the array by removing some (possibly all) elements of it
'''

# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()


def SubsetUtill(arr,index,current_Subset,res):
    # include all the element in the result
    # base case : if we consider all the element
    if index == len(arr):
        res.append(current_Subset[:])
        return
    
    # case 1 : have to exclude the element itself
    SubsetUtill(arr,index + 1,current_Subset,res)
    
    # case 2 : have to include the current element
    current_Subset.append(arr[index])
    SubsetUtill(arr,index+1,current_Subset,res)
    
    # backtrack for remove the current element from the sol
    current_Subset.pop()
    
    
# main function
def SubsetGenerator(arr):
    index = 0
    current_Subset = []
    res = []
    res = SubsetUtill(arr,0,current_Subset,res)



arr = map(list,int(input("enter element :")))
res = SubsetGenerator(arr)

print(f"The main array is : {arr}")    
logging.info(f"The main array is : {arr}")


print(f"The subset of the array is : {res}")
logging.info(f"The subset of the array is : {res}")