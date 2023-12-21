'''
Given an array of elements of length N, ranging from 0 to N – 1.
All elements may not be present in the array. 
If the element is not present then there will be -1 present in the array.
Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.

'''
def rearrange(arr):
    n = len(arr)
    arr.sort()
    test = []
    for i in range(n):
        if i in arr:
            test.append(i)
        else:
            test.append(-1)
            
    print(test)
            
            
arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
rearrange(arr)


