# find the  range min  query for the giben array
def range_min_query(arr,l,r):
    n = len(arr)
    if n > l and n > r:
        return min(arr[l:r])
    else:
        return -1
    
    
# test operation
a = [7, 2, 3, 0, 5, 10, 3, 12, 18] 
print(f"The min of the query 0 -4 is : {range_min_query(a,4,7)}")