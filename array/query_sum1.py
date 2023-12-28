'''

We are given an array and a set of query ranges, we are required to find the sum of every query range.

Example: 

Input:  arr[]   = {1, 1, 2, 1, 3, 4, 5, 2, 8};
        query[] = [0, 4], [1, 3] [2, 4]
Output: Sum of arr[] elements in range [0, 4] is 8
        Sum of arr[] elements in range [1, 3] is 4  
        Sum of arr[] elements in range [2, 4] is 6
        
'''
import math
# brute force approach
def brute_query_sum(arr,Q):
    for q in Q:
        L,R = q
        s = 0
        for i in range(L,R+1):
            s+=arr[i]
        print(f"The sum of {L} to {R} range is : {s}")
        


# using the most simplest method

# it is called the MO's algorithm
def simple_query_sum(arr,Q):
    # first sort the query array
    Q.sort(key = lambda x: x[1])
    
    # after sorting storage of left and right and current sum of the array
    currL,currR,currSum = 0 ,0 , 0
    
    # after that have to following steps
    
    # 1. loop through the array
    for i in range(len(Q)):
        L,R = Q[i]
        
        #remove the extra space from the sum
        while currL < L:
            currSum-=arr[currL]
            currL+=1
            
            
        # add the element when it meets the condition
        while currL > L:
            currSum+=arr[currL-1]
            currL-=1
        while currR <= R:
            currSum+=arr[currR]
            currR+=1
            
            
        # remove the extra element from the right side
        while currR > R+1:
            currSum-=arr[currR-1]
            currR-=1
            
        # print the output of the result
        print(f"The sum of the query of the range {L} to {R} : {currSum}")
            
        
        

# input
arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
Q = [[0, 4], [1, 3], [2, 4]]
brute_query_sum(arr,Q)
simple_query_sum(arr,Q)
        
        

            
    