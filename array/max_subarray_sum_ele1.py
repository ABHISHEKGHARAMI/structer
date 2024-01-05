# max sub array which returns the sum as well as the element as well

# kadane's  approach for max sum
#dyanmic
def kadane(arr):
    n = len(arr)
    max_so_far = arr[0]
    max_ending_here = 0
    for i in range(n):
        max_ending_here+=arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kadane(a))
            
