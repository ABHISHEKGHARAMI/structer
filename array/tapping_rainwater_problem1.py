'''
Given an array of N non-negative integers arr[] representing an elevation map 
where the width of each bar is 1,
compute how much water it is able to trap after raining.

'''
def naive_trapping(arr):
    res = 0
    
    n = len(arr)
    # For every element of the array 
    for i in range(1, n - 1): 
  
        # Find the maximum element on its left 
        left = arr[i] 
        for j in range(i): 
            left = max(left, arr[j]) 
  
        # Find the maximum element on its right 
        right = arr[i] 
  
        for j in range(i + 1, n): 
            right = max(right, arr[j]) 
  
        # Update the maximum water 
        res = res + (min(left, right) - arr[i]) 
    
    return res

# but this O(n*2) solution so has  to avoid this in a heartbreak
def eff_trapping(arr,n):
    water = 0
    left = [0]*n
    right = [0]*n 
    # fill the left array
    left[0] = arr[0]
    for i in range(1,n):
        left[i] = max(left[i-1],arr[i])
        
    # similarity for the right array
    right[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        right[i] = max(right[i+1],arr[i])
        
    for i in range(n):
        water+=min(left[i],right[i])-arr[i]
    return water
           
# try to execute the function
rain = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f"The maximum drop of rain can be stored is : {naive_trapping(rain)}")
print(f"The maximum drop water is :{eff_trapping(rain,len(rain))}")