'''

MERGE SORT
    it is not an inplace sorting algorithm
    Merge Sort is a Divide and Conquer algorithm. 
    It divides the input array in two halves, calls itself for the two halves and then merges 
    the two sorted halves. The merge() function is used for merging two halves.
    The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r]
    are sorted and merges the two sorted sub-arrays into one in a sorted manner. 
    See following implementation for details:
'''


def mergeSort(arr):
    n = len(arr)
    mid = n //2
    l = arr[:mid]
    r = arr[mid+1:]
    i , j , k = 0 , 0 , 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i+=1
        else:
            arr[k] = r[j]
            j+=1
            
        k+=1
    
    while i < len(l):
        arr[k] = l[i]
        i+=1
        k+=1
        
    while j < len(r):
        arr[k] = r[j]
        j+=1
        k+=1

    

arr = [3,2,6,4,-1,0,9]

mergeSort(arr)
print(arr)