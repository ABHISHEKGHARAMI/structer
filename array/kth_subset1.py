'''
Given an array of integers. Write a program to find the K-th largest sum of contiguous 
subarray within the array of numbers that has both negative and positive numbers.

'''
# try6 to print all subset of an array

import math
def subsetUtill(arr):
    n = len(arr)
    subset = []
    for start in range(n):
        for end in range(start+1,n+1):
            subset.append(arr[start:end])
    return subset


# kth subset for the given subset found from the array
def kth_max(arr,k):
    n = len(arr)
    sum = []
    subsets = subsetUtill(arr)
    for i in range(len(subsets)):
        sum.append(sum(subsets[i]))
    sum.sort()
    return sum[len(sum)-1-k]

# brute force approach
def kth_sum_max(arr,k):
    n = len(arr)
    result = []
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum +=arr[j]
            result.append(sum)
    result.sort(reverse = True)
    return result[k-1]


arr = [20, -5, -1]
k = 2
print(f"all the subsets are as follow : {subsetUtill(arr)}")
print(f"The {k} th maximum sum of the subarray is : {kth_sum_max(arr,k)}")

        
    