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
    
arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
x = 5
a,b = first_last_naive(arr,x)
print(f"The first and last occurence of {x} is : {a} , {b} ")
    