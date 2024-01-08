'''

Given an array a[] of N integers, the task is to find the length of the longest
Alternating Even Odd subarray present in the array. 

Examples: 

Input: a[] = {1, 2, 3, 4, 5, 7, 9} 
Output: 5 
Explanation: 
The subarray {1, 2, 3, 4, 5} has alternating even and odd elements.

'''
def evenOddSubarray(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i]%2 == 0 and arr[i+1] %2 != 0 or arr[i]!= 0 and arr[i+1] == 0:
            count+=1
        else:
            break
            
   
    return count
    
    
arr = [1, 2, 3, 4, 5, 7, 9]
print(f"The number of element present is : {evenOddSubarray(arr)}")
        