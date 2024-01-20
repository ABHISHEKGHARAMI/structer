'''

Given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array. Traverse array only once.
Examples: 

Input :  arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output : arr[] = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 

Input :  arr[] = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1] 
Output : arr[] = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]  


'''

def segregation(arr):
    n = len(arr)
    zero = 0
    one = n - 1
    while zero < one:
        if arr[zero] < arr[one]:
            arr[zero] , arr[one] = arr[one] , arr[zero]
            one = one - 1
        else:
            zero = zero + 1
            
arr = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1]
segregation(arr)
print(arr)
    