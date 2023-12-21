# correct the order of the even or odd of the given array
def correct_position(arr):
    even = []
    odd = []
    n = len(arr)
    for i in range(n):
        if arr[i]%2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()        
    arr.clear()
    j = 0
    k = 0
    for i in range(n):
        if i%2 == 0 and j < len(even):
            arr.append(even[j])
            j+=1
        elif i%2!= 0 and k<len(odd):
            arr.append(odd[k])
            k+=1
            
    print("After changing the position of the even or odd.")
    print(arr)


arr = [1, 2, 2, 1] 
correct_position(arr)           
            