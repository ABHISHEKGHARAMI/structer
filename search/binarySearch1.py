'''

Problem: Given a sorted array arr[] of n elements,
write a function to search a given element x in arr[] and return the index of x in the array.

                 Consider array is 0 base index.

Examples: 

Input: arr[] = {10, 20, 30, 50, 60, 80, 110, 130, 140, 170}, x = 110
Output: 6
Explanation: Element x is present at index 6. 

Input: arr[] = {10, 20, 30, 40, 60, 110, 120, 130, 170}, x = 175
Output: -1
Explanation: Element x is not present in arr[].


'''

def binarySearch(arr,start,end,x):
    if start <= end:
        mid  = (start + end) // 2
        if arr[mid] == x :
            return mid
        elif arr[mid] > x:
            return binarySearch(arr,start,mid-1,x)
        else:
            return binarySearch(arr,mid+1,end,x)
    else:
        return -1
    
    
    
arr = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
x = 110
pos = binarySearch(arr,0,len(arr)-1,x)

if pos!=-1:
    print(f"The position of {x} is : {pos+1}")
else:
    print(f"{x} is not found in the array...")
    
 