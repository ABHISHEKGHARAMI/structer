'''
Given a sorted array arr[] with possibly duplicate elements,
the task is to find indexes of the first and last occurrences of an element x in the given array. 

Examples: 

Input : arr[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}, x = 5
Output : First Occurrence = 2
              Last Occurrence = 5

Input : arr[] = {1, 3, 5, 5, 5, 5, 7, 123, 125 }, x = 7

Output : First Occurrence = 6
              Last Occurrence = 6
              
'''

# naive approach
def first_last_naive(arr,x):
    n = len(arr)
    first = -1
    last = -1
    for i in range(n-1):
        if x!=arr[i]:
            continue
        if first == -1:
            first = i
        last = i
    
    if first!= -1:
        return first,last
    else:
        return -1,-1

# first and last occurence using binary search
def first_binarySearch(arr,low,high,x,n):
   if high >= low:
       mid = low + (high - low) //2
       if mid == 0 or x> arr[mid-1] and arr[mid] == x:
           return mid
       elif x > arr[mid]:
           return first_binarySearch(arr,mid+1,high,x,n)
       else:
           return first_binarySearch(arr,low,mid-1,x,n)
   else:
       return -1
            
def last_binarySearch(arr,low,high,x,n):
    if high >= low:
        mid = low + (high - low) // 2
        if mid == n-1 or x < arr[mid+1] and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return last_binarySearch(arr,low,mid-1,x,n)
        else:
            return last_binarySearch(arr,mid+1,high,x,n)
    else:
        return -1
# utility function
def utility_first_last(arr,x):
    n = len(arr)
    a = first_binarySearch(arr,0,n-1,x,n)
    b = last_binarySearch(arr,0,n-1,x,n)
    if a!= 0 and b!=0:
        return a,b
    else:
        return -1,-1

arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
x = 5
a,b = first_last_naive(arr,x)
print(f"The first and last occurence of {x} is : {a} , {b} ")

c,d = utility_first_last(arr,x)
print(f"The first and last occurence using binary search is : {c} and {d}")
    