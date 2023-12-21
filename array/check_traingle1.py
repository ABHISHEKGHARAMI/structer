'''
Given an unsorted array of positive integers, 
find the number of triangles that can be formed with three different array 
elements as three sides of triangles. For a triangle to be possible from 3 values, 
the sum of any of the two values (or sides) must be greater than the third value (or third side).

'''
def check_traingle(arr):
    n = len(arr)
    count = 0 
    arr.sort()
    for i in range(n-2):
        j = i+1
        k = i+2
        while j < n and k < n:
            if arr[i]+arr[j] > arr[k]:
                count+=1
            j+=1
            k+=1
    return count

arr = [10, 21, 22, 100, 101, 200, 300]
print(f"the number of triangle is : {check_traingle(arr)}")



    