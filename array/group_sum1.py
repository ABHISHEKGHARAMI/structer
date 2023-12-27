'''

Given an array arr[] of size n and an integer X. 
Find if there’s a triplet in the array which sums up to the given integer X.

'''

# using the naive approach

def naive_group_sum(arr,data):
    n = len(arr) 
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == data:
                    return True
    return False



# two pointer technique

def two_pointer_group_sum(arr,sum):
    arr.sort()
    n = len(arr)
    for i in range(n-2):
        l = i + 1
        r = n - 1
        while l <= r:
            if arr[i] + arr[l] + arr[r] == sum :
                return True
            if arr[i] + arr[l] + arr[r] < sum :
                l+=1
            else:
                r=r-1
    return False
    

A = [1, 4, 45, 6, 10, 8]
sum = 22

if two_pointer_group_sum(A,sum) == True:
    print(f"The {sum} is present in the List.")
else:
    print(f"The {sum} is not present in the List.")