# insertion sort
'''
concept:
this is inplace sorting algorithm that requires constant or limited memory
space for specific operation

the concept behind the insertion sorting is that it continues to sort 
'''

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i-1):
            if arr[j] > arr[i]:
                arr[i],arr[j] = arr[j] , arr[i]
                
    # printing the arrray
    for i in range(n):
        print(arr[i],end=" ")
        

# time complexity O(n*2)
# main function
arr = [12, 11, 13, 5, 6,-1]
insertion_sort(arr)
        