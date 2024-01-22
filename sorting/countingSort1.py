'''
Counting sort algorithm
1.  Find the maximum value of the array
2.  declare an array with size of of max + 1 with the value of 0
3.  Store the count of each element in the count array
4.  Store the cummulative sum of the each of the element of the count array.
5. then have to get the elemnt from  the original array and find the index of it in the 
   count array then replace with correct position in the output array.
'''

def countingSort(arr):
    n = len(arr)
    max1 = max(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        count[arr[i]]+=1
        
    # cummulative sum of the count array
    for i in range(1,10):
        count[i] += count[i-1]
        
    i = n -1
    while i >= 0:
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]]-=1
        i=i-1
    
    
    for i in range(n):
        arr[i] = output[i]
    
    
# main function
arr = [4, 2, 2, 8, 3, 3, 1]
countingSort(arr)
print(arr)
        
    
        
    
    
    
    
    