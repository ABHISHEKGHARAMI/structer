'''
Given a sorted array of positive integers. 
Your task is to rearrange the array elements alternatively 
i.e first element should be max value,
second should be min value, third should be second max, 
fourth should be second min and so on.

n = 6
arr[] = {1,2,3,4,5,6}
Output: 6 1 5 2 4 3

'''

def rearrange(arr):
    n = len(arr)
    if n==1:
        return arr[0]
    l = []
    for i in range((n+1)//2):
        l.append(arr[n-i-1])
        l.append(arr[i])
    for i in range(n):
        arr[i] = l[i]
    return arr
arr = [1,2,3,4,5,6]
print(f"The arranged array is : {rearrange(arr)}")


    