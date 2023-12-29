'''

Given an array of n elements. We need to answer q 
queries telling the sum of elements in range l to 
r in the array. Also the array is not static i.e 
the values are changed via some point updateQuery.

Range Sum Queries are of form : Q l r , 
where l is the starting index r is the ending index

Point updateQuery is of form : U idx val, 
where idx is the index to update val is the 
updated value.

'''

from math import sqrt

MAXN = 10000
SQRSIZE = 100

arr = [0]*(MAXN)         # original array
block = [0]*(SQRSIZE)
blc_size = 0

def update(idx,val):
    blockNumber = idx // blc_size
    block[blockNumber]+=val - arr[idx]
    arr[idx] = val
    
#Query for process
def Query(l,r):
    sum = 0
    while l < r and l%blc_size!=0 and l!=0:
        # traversing through array
        sum+=arr[l]
        l+=1
        
    # traverse completely overlapping 
    while l+blc_size-1 <= r:
        # traversing completely to r
        sum+=block[l//blc_size]
        l+=blc_size
        
    while l <= r:
        sum+=arr[l]
        l+=1
        
    return sum

def preprocess(input,n):
    blk_idx = -1
    global blc_size
    blc_size = int(sqrt(n))
    for i in range(n):
        arr[i] = input[i]
        if i%blc_size == 0:
            blk_idx +=1
        block[blk_idx]+=arr[i]
        
        
input = [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
n = len(input)
preprocess(input,n)
print("Query(3,8) : ",Query(3, 8))
print("Query(1,6) : ",Query(1, 6))
update(8, 0)
print("Query(8,8) : ",Query(8, 8))

        
    

