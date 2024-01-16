# Hoare Partition for Quick Sort

# in this algorithm we will take the first element as the pivot

'''
Hoare’s Partition Scheme works by initializing two indexes that start at two ends, 
the two indexes move toward each other until an inversion is (A smaller value on the
left side and a greater value on the right side) found. When an inversion is found, 
two values are swapped and the process is repeated.

Algorithm: 

Hoarepartition(arr[], lo, hi)

   pivot = arr[lo]
   i = lo - 1  // Initialize left index
   j = hi + 1  // Initialize right index

   // Find a value in left side greater
   // than pivot
   do
      i = i + 1
   while arr[i] < pivot

   // Find a value in right side smaller
   // than pivot
   do
      j--;
   while (arr[j] > pivot);

   if i >= j then 
      return j

   swap arr[i] with arr[j]


   
QuickSort(arr[], l,  r)

If r > l
     1. Find the partition point of the array  
              m =Hoarepartition(a,l,r) 
     2. Call Quicksort for less than partition point   
             Call Quicksort(arr, l, m)
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
    pivot = arr[low]
    k = high
    for j in range(high,low,-1):
        if arr[j] > pivot :
            arr[j] , arr[k] = arr[k] , arr[j]
            k = k - 1
    arr[k] , arr[low] = arr[low] , arr[k]
    return k



# main function for the quick sort
arr = [10, 9,7,4,3,1,0]

QuickSort(arr,0,len(arr)-1)

print("After quick sort the array will be :")
print(arr)