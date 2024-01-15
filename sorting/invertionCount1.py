'''

Inversion Count for an array indicates – how far (or close) the array is from being sorted. 
If the array is already sorted, then the inversion count is 0, but if the array is sorted
in reverse order, the inversion count is the maximum. 

Given an array a[]. The task is to find the inversion count of a[].
Where two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Examples: 

Input: arr[] = {8, 4, 2, 1}
Output: 6
Explanation: Given array has six inversions: (8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).


'''


# naive approach

def naive_invertionCount(arr):
    n = len(arr)
    icount = 0
    for i in range(n-1):
        for j in range(n):
            if arr[i] > arr[j]:
                icount+=1
    return icount


arr = [8, 4, 2, 1]

print(f"The Invertion count of the array is : {naive_invertionCount(arr)}")