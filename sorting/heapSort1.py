'''Heap Sort in python

Algorithm for heapSort

1. first build the max heap
2. then preform the sort operation'''

def heapify(arr,n,i):
    # first after largest
    largest = i
    # left child for the node
    left_child = 2 * i + 1
    # right child for the node
    right_child = 2 * i + 2
    
    if left_child < n and arr[left_child] > arr[largest] :
        largest = left_child
        
    # check for the right child
    if right_child < n and arr[right_child] > arr[largest] :
        largest = right_child
        
    # check for the largest 
    if largest != i:
        arr[i] , arr[largest] = arr[largest] , arr[i]
        heapify(arr,n,largest)
        
        
# heap sort for main function

def heapSort(arr):
    n = len(arr)
    
    #first build the heapify
    for i in range(n//2 - 1 , -1, -1):
        heapify(arr,n,i)
        
    # extract the elements
    for i in range(n - 1, -1, -1):
        arr[i] , arr[0] = arr[0] , arr[i]
        heapify(arr,i,0)
        
        
# example for the usage of the array

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print(f"After the heapSort the array will be : {arr}")