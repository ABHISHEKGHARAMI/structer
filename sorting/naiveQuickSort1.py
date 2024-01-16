# Naive Quick Sort Algorithm 
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