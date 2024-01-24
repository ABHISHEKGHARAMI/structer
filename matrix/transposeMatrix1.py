''' Transpose of an matrix. '''

# using the brute force approach for the matrix

def bruteTranspose(mat):
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        for j in range(i+1 , n):
            mat[i][j], mat[j][i] = mat[j][i] , mat[i][j]
                
    # print the matrix
    for i in range(m):
        for j in range(n):
            print(mat[i][j] , end = " ")
        print("\n")
mat = [[1,2,3],[4,5,6],[7,8,9]]
bruteTranspose(mat)
    