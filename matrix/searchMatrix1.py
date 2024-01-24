'''Search in the matrix.'''

def searchMatrix(mat,x):
    m = len(mat)
    n = len(mat[0])
    flag = 0
    row , column = 0 , 0
    
    # search for the element in the array
    for i in range(m):
        for j in range(n):
            if mat[i][j] == x:
                row , column = i , j
                flag = 1
            
                break
            break
    
    # flag changing
    if flag == 1:
        return row+1 , column+1
    else :
        return row , column
    
    
mat = [[1,2,3],[4,5,6],[7,8,9]]
x = 7
if searchMatrix(mat,x) != 0:
    print(f"The {x} present in the matrix is : {searchMatrix(mat,x)}")
else:
    print("The {x}  not present in the matrix . ")