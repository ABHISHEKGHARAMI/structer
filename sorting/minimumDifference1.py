'''


Find minimum difference between any two elements (pair) in given array

Given an unsorted array, find the minimum difference between any pair in the given array.

Examples :

 

Input: {1, 5, 3, 19, 18, 25}
Output: 1
Explanation: Minimum difference is between 18 and 19

Input: {30, 5, 20, 9}
Output: 4
Explanation: Minimum difference is between 5 and 9

Input: {1, 19, -4, 31, 38, 25, 100}
Output: 5
Explanation: Minimum difference is between 1 and -4.


'''


# naive approach 

def minDifference(arr):
    n = len(arr)
    min = 999999
    for i in range(n-1):
        j = i + 1
        while j < n:
            if abs(arr[j] - arr[i]) < min :
                min = abs(arr[j] - arr[i])
            j+=1
    return min



# more efficient approach


def QuickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)
        
        
# partition for quicksort
def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1
        


#  now for the min difference 
def minEffDifference(arr):
    n = len(arr)
    QuickSort(arr,0,n-1)
    min = 99999
    for j in range(n-1):
        if abs(arr[j+1]-arr[j]) < min:
            min = abs(arr[j+1] - arr[j])
    return min
arr = [1, 19, -4, 31, 38, 25, 100]

print(f"The minimum value of the difference is : {minDifference(arr)}")
print(f"The minimum value of the efficient approach is :{minEffDifference(arr)}")