'''

Given an array arr[] of n integers. Check whether it contains a triplet that sums up to zero. 

Note: Return 1, if there is at least one triplet following the condition else return 0.

'''


def findTriplet(arr):
    n = len(arr)
    flag = 0
    i = 0
    while i < n-2:
        j = i+1
        k = n-1
        if arr[i] + arr[j] + arr[k] == 0:
            flag = 1
            break
        else:
            j = j + 1
            k = k - 1
        
        i+=1
    if flag == 1:
        return 1
    else:
        return 0
    
    
arr = [ 0, -1, 2, 1, -3]
if findTriplet(arr) == 1:
    print("Triplet found in the array")
else:
    print("No triplte found in the array.")