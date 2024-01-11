"""

Given an unsorted array A of size N that contains only non negative integers, 
find a continuous sub-array that adds to a given number S and return 
the left and right index(1-based indexing) of that sub array.

In case of multiple sub arrays, return the sub array indexes which come first
on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements left and right. 
In case no such sub array exists return an array consisting of element -1.

Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.
Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.

"""

# two pointer solution
def two_pointer(arr,target_sum):
    left = 0
    current_sum = 0
    n = len(arr)
    result = []
    for right in range(n):
        current_sum+= arr[right]
        
        while current_sum > target_sum:
            current_sum-= arr[left]
            left+=1
        
        if target_sum == current_sum:
            result = [left+1,right+1]
            
    if not result:
        return [-1]
    return result
            
            
        
        

arr = [1,2,3,7,5]
s = 15
print(f"The first , last index of the array is : {two_pointer(arr,s)}")

                
                