'''

Given a sorted array of n distinct integers where each integer is in the range
from 0 to m-1 and m > n.
Find the smallest number that is missing from the array. 

'''
# modify the binary search 
# use the technique for search the i if present then return i else return 0
# this algo does not work for data repeating itself
def smallest_missing(arr,start,end):
    if start > end:
        return end+1
    if start != arr[start]:
        return start
    mid = (start+end)//2
    if arr[mid] == mid:
        return smallest_missing(arr,mid+1,end)
    return smallest_missing(arr,start,mid)


# due to this problem have to change the approach
def find_sorted_missing(arr):
    if arr[0]!=0:
        return 0
    if arr[-1] == len(arr)-1 :
        return len(arr)
    first = arr[0]
    
    return findMissing(arr,0,len(arr)-1,first)


# recursive binary search
def findMissing(arr,start,end,first):
    if start < end:
        mid = (start + end)//2
        
        if arr[mid] != first + mid :
            return findMissing(arr,start,mid,first)
        else:
            return findMissing(arr,mid+1,end,first)
    return start +  first
    

arr = [0, 1, 2, 3, 4, 5, 6, 7, 10]

print(f"the smallest missing number present in the array is : {smallest_missing(arr,0,len(arr)-1)}")
print(f"The smallest missing number present in the array in recursive : {find_sorted_missing(arr)}")