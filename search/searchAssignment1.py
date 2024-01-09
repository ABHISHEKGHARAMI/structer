'''
Description: Given an unsorted array of size n. Array elements are in the range from 1 to n.
One number from set {1, 2, …n} is missing and one number occurs twice in the array. 
Our task is to find these two numbers.
 

Input
[2, 3, 2, 1, 5]
Output
4 2

'''
from collections import Counter

# binary search

def binarySearch(arr,low,high,x):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr,low,mid-1,x)
        else:
            return binarySearch(arr,mid+1,high,x)
    else:
        return -1

def counterTwo(arr):
    dict1 = Counter(arr)
    d1 = []
    for i in dict1:
        if dict1[i] == 2:
            d1.append(i)
    return d1[0]

# main util function
def SearchAssignment(arr):
    arr.sort()
    m1 = 0
    flag = 0
    c2 = counterTwo(arr)
    low = arr[0]
    high = arr[len(arr) - 1]
    for i in range(low,high):
        if binarySearch(arr,0,len(arr)-1,i) == -1:
            m1 = i
            flag = 1
            break
    if flag == 1:
        return m1,c2
    else:
        return 0,0
    
    
    
arr = [2, 3, 2, 1, 5]

a , b = SearchAssignment(arr)

if a != 0 and b != 0:
    print(f"the missing number is {a} and the number that appears twice is {b}")
else:
    print(f"the missing number is : {a} and the number twice appears is {b}")