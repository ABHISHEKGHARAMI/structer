# matrix spiral rotation for the matrix

def matrixSpiral(mat):
    k , l = 0 , 0
    m , n = len(mat) , len(mat[0])
    while k < m and l < n :
        # for upper part of matrix row
        for i in range(l,n):
            print(mat[k][i],end=" ")
        k += 1
        
        # for back part of the matrix column
        for i in range(k,m):
            print(mat[i][n-1],end=" ")
        n = n - 1
        
        # for last row of the matrix row
        if k < m :
            i = n - 1
            while i >= l:
                print(mat[m-1][i],end=" ")
                i = i - 1
            m = m - 1
        # for the first column printing
        if l < n:
            i = m - 1
            while i >= k:
                print(mat[i][l],end=" ")
                i = i - 1
            l += 1
            
            
# print the matrix
mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrixSpiral(mat)