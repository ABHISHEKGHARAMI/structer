# Bubble sort
'''
This is a inplace algorithm

concept is that
In one iteration if we swap all adjacent elements of an array such that after swap the
first element is less than the second element then at the end of the iteration, 
the first element of the array will be the minimum element.
 



Bubble-Sort algorithm simply repeats the above steps N-1 times, where N is the size of the array.

Example: Consider the array, arr[] = {5, 1, 4, 2, 8}.
 

First Pass: ( 5 1 4 2 8 ) --> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements,
and swaps since 5 > 1. ( 1 5 4 2 8 ) -->  ( 1 4 5 2 8 ),
Swap since 5 > 4 ( 1 4 5 2 8 ) -->  ( 1 4 2 5 8 ), 
Swap since 5 > 2 ( 1 4 2 5 8 ) --> ( 1 4 2 5 8 ), Now, since these elements are already in order 
(8 > 5), algorithm does not swap them.
Second Pass: ( 1 4 2 5 8 ) --> ( 1 4 2 5 8 ) ( 1 4 2 5 8 ) --> ( 1 2 4 5 8 ),
Swap since 4 > 2 ( 1 2 4 5 8 ) --> ( 1 2 4 5 8 ) ( 1 2 4 5 8 ) -->  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed.
The algorithm needs one whole pass without any swap to know it is sorted.
Third Pass: ( 1 2 4 5 8 ) --> ( 1 2 4 5 8 ) ( 1 2 4 5 8 ) --> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) --> ( 1 2 4 5 8 ) ( 1 2 4 5 8 ) --> ( 1 2 4 5 8 )

'''

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
    # print all the element
    for i in range(n):
        print(arr[i],end=" ")
        
# main function
arr = [5, 1, 4, 2, 8, -1,-100]

bubbleSort(arr)
