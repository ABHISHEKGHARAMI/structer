'''
Radix Sort algorithm for list


first find the maximum element of the array then do the counting sort


'''
import math

def radixSort(arr):
    n = len(arr)
    exp = 1
    max1 = max(arr)
    while max1 // exp > 0:
        countingSort(arr,exp)
        exp = exp * 10
        
        
# counting sort util for the radix sort
def countingSort(arr,exp):
    n = len(arr)
    output = [0] * (n + 1)
    count = [0] * 10
    
    # for inserting every element in the array
    for i in range(n):
        index = arr[i] // exp
        count[index %10]+=1
        
    # cummelative sum for the array
    for i in range(1,10):
        count[i] += count[i-1]
        
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[math.floor(index%10) - 1]] = arr[i]
        count[index%10]-=1
        i-=1
    
    # storing the output of the value
    for i in range(n):
        arr[i] = output[i]
        
        

# main function for the radix sort algorithm 
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
print(f"After Radix sort the output will be : {arr}")