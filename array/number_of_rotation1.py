'''
Given an array arr[] of size N having distinct numbers sorted in increasing order and 
the array has been right rotated (i.e, the last element will be cyclically shifted to the starting
position of the array) k number of times,
the task is to find the value of k.

'''

def numberOfRotation(arr):
    # let say that if that is rotated then any time that left element is 
    # greater than the right element then count when it appears
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[i+1] and i+1 < n :
            return i+1
        
        

        

def rotationByOne(arr):
    n = len(arr)
    temp = arr[n-1]
    res = arr[0:n-1]
    res.insert(0,temp)
    return res
    

arr = [15, 18, 2, 3, 6, 12]
print(f"The number of rotation for getting it : {numberOfRotation(arr)}")
