# find the largest sum of the given array
def find_large_sub(arr):
    n = len(arr)
    sum1 = 0
    for i in range(n):
        for j in range(i+1,n+1):
            sum1.append(sum(arr[i:j]))
            
    return max(sum1) 


arr = [ 1,4,5,9,-1]
print(f"The largest subarray sum is : {find_large_sub(arr)}")
   