# find the second largest element of the array
def second_largest(arr):
    n = len(arr)
    first = -9999999
    second = -9999999
    for i in range(1,n):
        # if the large 
        if arr[i] > first:
            second = first
            first = arr[i]
            
        elif arr[i] > second and arr[i]!=first:
            second = arr[i]
            
    return second

arr = [12, 35, 1, 10, 34, 1]

print(f"The second element of the array is : {second_largest(arr)}")