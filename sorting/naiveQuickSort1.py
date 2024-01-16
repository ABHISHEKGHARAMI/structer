# Naive Quick Sort Algorithm 


'''
The key process in quickSort is a partition(). 
The target of partitions is to place the pivot (any element can be chosen to be a pivot) 
at its correct position in the sorted array and put all smaller elements to the left of the pivot,
and all greater elements to the right of the pivot.

Partition is done recursively on each side of the pivot after the pivot 
is placed in its correct position and this finally sorts the array.



sudo algorithm :

Naive partition(arr[],l,r)
1. Make a Temporary array temp[r-l+1] length
2. Choose last element as a pivot element
3. Run two loops:
    -> Store all the elements in the temp array that are less than pivot element
    -> Store the pivot element 
    -> Store all the elements in the temp array that are greater than pivot element.
4.Update all the elements of arr[] with the temp[] array    


QuickSort(arr[], l,  r)
If r > l
     1. Find the partition point of the array  
              m = Naivepartition(a,l,r) 
     2. Call Quicksort for less than partition point   
             Call Quicksort(arr, l, m-1)
     3. Call Quicksort for greater than the partition point 
             Call Quicksort(arr, m+1, r)

'''
def QuickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)
        
        
# partition for the quick sort
def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i + 1


# main function for naive quick sort function
arr = [10,9,7,4,3,1,0]
QuickSort(arr,0,len(arr)-1)
print("After the quick sort the array is :")
print(arr)