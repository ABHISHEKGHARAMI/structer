'''
Given three sorted arrays A, B and C of size N, M and P respectively. 
The task is to merge them into a single array which must be sorted in increasing order.

N = 4, A[] = [1 2 3 4] 
M = 5, B[] = [1 2 3 4 5] 
P = 6, C[] = [1 2 3 4 5 6]
Output: 1 1 1 2 2 2 3 3 3 4 4 4 5 5 6

'''

def mergeThreeSort(a,b,c):
    n1 = len(a)
    n2 = len(b)
    n3 = len(c)
    arr = []
    i = j = k = 0
    while i < n1 and j < n2 and k < n3:
        if a[i] <= b[j] and a[i] <= c[k]:
            arr.append(a[i])
            i+=1
        elif b[j] <= a[i] and b[j] <= c[k]:
            arr.append(b[j])
            j+=1
        else:
            arr.append(c[k])
            k+=1
            
    while i < n1:
        arr.append(a[i])
        i+=1
    
    while j < n2:
        arr.append(b[j])
        j+=1
        
    while k < n3:
        arr.append(c[k])
        k+=1
        
    
    return arr



# main function
a = [1,2,3,4]
b = [1,2,3,4,5]
c = [1,2,3,4,5,6]

print(mergeThreeSort(a,b,c))