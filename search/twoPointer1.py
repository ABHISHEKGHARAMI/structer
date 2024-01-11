# here we learn to use two pointer approach
# first we try to write down the naive approach

def naive(arr,x):
    flag = 0
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] + arr[j] == x:
                flag = 1
                break
    if flag == 1:
        return True
    else:
        return False
    
    
arr = [ 2,3,8 ,11]
x = 14

if naive(arr,x) == 1:
    print("Pair.")
else:
    print("Dont have pair.")