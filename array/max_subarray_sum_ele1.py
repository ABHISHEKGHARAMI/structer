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


# program for the return the elemnet of the array form the original array
def element_kadane(arr):
    if not arr:
        return 0,[]
    else:
        max_sum = current_sum = arr[0]
        start = end = 0
        current_state = 0
        
        for i in range(1,len(arr)):
            if arr[i] > current_sum+arr[i]:
                current_sum = arr[i]
                current_start = i
            else:
                current_sum+=arr[i]
            
            if current_sum > max_sum:
                max_sum = current_sum
                start = current_start
                end = i
        
        return max_sum , arr[start:end+1]
    
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kadane(a))
c , b = element_kadane(a)
print(f"The max sum is : {c} and the array giving the sum is : {b}")