'''
We are given an sorted boolean array, We have to find out the index of first 1 in the Array

Input : arr[] = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
Output : 6
The index of first 1 in the array is 6.

'''

def binarySearch(arr,low,high,x):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x and mid == 0 or arr[mid-1]==0:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr,low,mid-1,x)
        else:
            return binarySearch(arr,mid+1,high,x)
    else:
        return -1
    
arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

print(f"the first 1 found in the place of : {binarySearch(arr,0,len(arr)-1,1)}")