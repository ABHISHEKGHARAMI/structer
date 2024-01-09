'''
Given an array arr[] of integers. Find a peak element i.e. an element that 
is not smaller than its neighbors. 

Note: For corner elements, we need to consider only one neighbor. 

Example:

Input: array[]= {5, 10, 20, 15}
Output: 20
Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.

'''


# trying to solve it in naive approach

def peakElement(arr):
    d = []
    n = len(arr)
    for i in range(1,n-1):
        if arr[i] > arr[i-1] and arr[i]>arr[i+1]:
            d.append(arr[i])
            
    if len(d):
        return d
    else:
        return []
    
arr = [5, 10, 20, 15]
print(f"The peak element is : {peakElement(arr)}")