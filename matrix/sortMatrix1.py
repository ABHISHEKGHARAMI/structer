''' sort the matrix in python . '''

# Brute force approach for sort .

# Quick Sort 
def QuickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi + 1, high)
        
# partition for quicksort
def partition(arr,low,high):
    pivot = arr[low]
    k = high
    for j in range(high,low, -1):
        if arr[j] > pivot:
            arr[j],arr[k] = arr[k],arr[j]
            k = k - 1
    arr[k] , arr[low] = arr[low] , arr[k]
    return k

def sortMatrix(mat):
    arr = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            arr.append(mat[i][j])
    QuickSort(arr,0,len(arr)-1)
    # arrange for the matrix 
    k = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = arr[k]
            k+=1
    # print the matrix
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end = " ")
        print("\n")


# try out for the matrix
mat =  [[5,4,7], [1,3,8], [2,9,6]]
sortMatrix(mat)