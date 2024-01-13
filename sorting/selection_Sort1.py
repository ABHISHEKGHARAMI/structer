'''
Selection sort:
 selection sort is this  sorting process where the shortest element will be replaced first 
 according to its consecutive order
 
 concept:
  The selection sort algorithm sorts an array by repeatedly finding the minimum element 
  (considering ascending order) from unsorted part and putting it at the beginning. 
  The algorithm maintains two sub arrays in a given array.
 

The sub array which is already sorted.
Remaining sub array which is unsorted.


In every iteration of selection sort, the minimum element (considering ascending order)
from the unsorted sub array is picked and moved to the sorted sub array. 

'''

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]
        
    # print all the element
    for i in range(n):
        print(arr[i], end=" ")
        
        
        
# main function
arr = [5, 1, 4, 2, 8, -1,-100]
selectionSort(arr)
        