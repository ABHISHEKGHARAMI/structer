'''
Given information about N petrol pumps (say arr[]) that are present in a circular path.
The information consists of the distance of the next petrol
pump from the current one (in arr[i][1]) and the amount of petrol stored
in that petrol pump (in arr[i][0]). Consider a truck with infinite capacity 
that consumes 1 unit of petrol to travel 1 unit distance. 
The task is to find the index of the first starting point such that the truck 
can visit all the petrol pumps and come back to that starting point.

Note: Return -1 if no such tour exists.

Examples:

Input: arr[] = {{4, 6}, {6, 5}, {7, 3}, {4, 5}}. 
Output: 1
Explanation: If started from 1st index then a circular tour can be covered.

Input: arr[] {{6, 4}, {3, 6}, {7, 3}}
Output: 2
'''
# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging


setup_logging()

# find the starting point
def find_start_point(arr):
    n = len(arr)
    start = 0
    end = 0
    petrol_left = 0
    total_petrol = 0
    
    
    for i in range(n):
        total_petrol += arr[i][0]
        petrol_left += arr[i][0] - arr[i][1]
        
        
        if petrol_left < 0:
            start = i + 1
            petrol_left = 0
    if total_petrol < petrol_left:
        return -1
    return start


# execution for the main function
arr1 = [[6, 4], [3, 6], [7, 3]]
re = find_start_point(arr1)
print(f"The start point of the petrol and distance is : {re}")
logging.info(f"The start point of the petrol and distance is : {re}")