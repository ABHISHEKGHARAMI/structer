# print only the boundary wall of the matrix
def boundary(mat):
    k , l = 0 , 0
    m , n = len(mat) , len(mat[0])
    # for upper wall
    for i in range(l,n):
        print(mat[k][i])
    k+=1
    # for right wall
    for i in range(k,m):
        print(mat[i][n-1])
    n = n-1
    # for lower wall
    i = n - 1
    while i >= l:
        print(mat[m-1][i])
        i = i -1
    m = m - 1
    # for left wal
    i = m - 1
    while i >= l:
        print(mat[i][l])
        i = i - 1
    l = l + 1
    
    
# print the matrix
mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
boundary(mat)