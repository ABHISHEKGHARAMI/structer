'''
Given an array arr[] of integers, find out the maximum difference 
between any two elements such that larger element appears after the smaller number. 

'''
def naive_max_diff(arr):
    n = len(arr)
    max_diff = 0
    for i in range(n-1):
        for j in range(i+1,n):
            diff = arr[j] - arr[i]
            if diff > max_diff :
                max_diff = diff
                
    return max_diff





arr = [2, 3, 10, 6, 4, 8, 1]
print(f"The naive max difference is : {naive_max_diff(arr)}")
#print(f"The efficient max difference is : {eff_max_diff(arr)}")



            