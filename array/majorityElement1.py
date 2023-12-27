'''
Find the majority element in the array. A majority element in 
an array A[] of size n is an element that appears more than n/2 times 
(and hence there is at most one such element). 
'''
from collections import Counter

# using the dictionary key , value from the list

def majorityElement(arr):
    dict1 = Counter(arr)
    
    value = 0
    # loop
    max1 = -999999
    for x in dict1:
        if dict1[x] >= len(arr)//2:
            max1 = max(max1,dict1[x])
            value = x
    return value

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(f"The majority element in the array is : {majorityElement(arr)}")
