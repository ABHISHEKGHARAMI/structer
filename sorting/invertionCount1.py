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

# invertion using the merge sort
def mergeSort(arr):
    n = len(arr)
    temp = [0] * n
    return _mergeSort(arr,temp,0,n-1)


# modify the merge sort
def _mergeSort(arr,temp,left,right):
    icout = 0
    if left < right:
        mid = (right + left) // 2
        icout+= _mergeSort(arr,temp,left,mid)
        icout+= _mergeSort(arr,temp,mid+1,right)   
        icout+= merge(arr,temp,left,mid,right)
    return icout

# merge the sort for modification
def merge(arr,temp,left,mid,right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i+=1
            k+=1
        else:
            temp[k] = arr[j]
            inv_count += mid - i + 1
            j+=1
            k+=1
            
    while i <= mid :
        temp[k] = arr[i]
        i+=1
        k+=1
    while j <= right:
        temp[k] = arr[j]
        j+=1
        k+=1
        
    # loop for copying from the temporary array
    for i in range(left,right + 1):
        arr[i] = temp[i]
        
    return inv_count
        
        
    
    
arr = [8, 4, 2, 1]

print(f"The Invertion count of the array is : {mergeSort(arr)}")