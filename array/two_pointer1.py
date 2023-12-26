'''

Two pointers is really an easy and effective technique that is typically used for searching pairs 
in a sorted array.
Given a sorted array A (sorted in ascending order), having N integers, 
find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.

'''
# naive approach

def naive_pointer(arr,value):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if arr[i]+arr[j] == value:
                return True
    return False

# proper two pointer technique
def two_pointer(arr,value):
    i = 0
    n = len(arr)
    j = n-1
    while i < j:
        if i == j :
            continue
        if arr[i]+arr[j] == value:
            return True
        if arr[i] + arr[j] < value :
            i+=1
        else:
            j=j-1
    return False

arr = [2, 3, 5, 8, 9, 10, 11]
value =17

if two_pointer(arr,value) == 1:
    print(f"{value} is present in the array.")
else:
    print(f"{value} is not present in the array.")
