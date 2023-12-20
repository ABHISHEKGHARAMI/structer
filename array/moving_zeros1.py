# Moving zeros to the end
def moving_zero(arr):
    n = len(arr)
    a1 = []
    for i in range(n):
        if arr[i]!=0:
            a1.append(arr[i])
            
    m = len(a1)
    if n > m:
        for i in range(n-m):
            a1.append(0)
            
    print(a1)
    
    
# main function
arr = [1, 2, 0, 4, 3, 0, 5, 0]
moving_zero(arr)
##
        