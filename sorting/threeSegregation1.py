'''

Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the
given array. The functions should put all 0s first, then all 1s and all 2s in last.
Examples: 
 

Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}


'''

def threeSegregation(arr):
    n = len(arr)
    co1 , co2 , co3 = 0 , 0 , 0
    i = 0
    while i < n:
        if arr[i] == 0:
            co1+=1
            i+=1
        elif arr[i] == 1:
            co2+=1
            i+=1
        else:
            co3+=1
            i+=1
    temp = []
    for i in range(co1):
        temp.append(0)
    for i in range(co2):
        temp.append(1)
    for i in range(co3):
        temp.append(2)
        
    for i in range(n):
        arr[i] = temp[i]
        
        
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
threeSegregation(arr)
print(arr)