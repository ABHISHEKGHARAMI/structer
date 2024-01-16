# Hoare Partition for Quick Sort

# in this algorithm we will take the first element as the pivot

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