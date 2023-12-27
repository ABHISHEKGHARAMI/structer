'''
Given an array arr of n elements that is first strictly increasing and then maybe
strictly decreasing, find the maximum element in the array.

Input: array[]= {5, 10, 20, 15}
Output: 20

'''
def peak_utill(arr):
    n = len(arr)
    copy = []
    for i in range(n):
        copy.append(arr[i])
    if arr[1]-arr[0] > 0:
        if copy.sort() == arr:
            return arr[n-1]
    if arr[1] - arr[0] < 0:
        if copy.sort(reverse=True) == arr:
            return arr[0]
    if arr[1]-arr[0] > 0:
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                return arr[i-1]
    else:
        for i in range(n):
            if arr[i]>arr[i-1]:
                return arr[i-1]
        
# more efficient approch

def peakFinder(arr):
    l = 0
    h = len(arr)-1
    n = len(arr)-1
    while l <= h :
        mid  = (l + h) >> 1
        
        # first case where mid 
        if (mid == 0 or arr[mid-1] <= arr [mid] ) and (mid == n-1 or arr[mid+1] <= arr[mid]):
            break
        
        # move the right pointer
        if mid > 0 and arr[mid-1] > arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
            
    return mid

arr = [1, 3, 20, 4, 1, 0]

print(f"The peak element of the array is : {arr[peakFinder(arr)]}")
