'''Traverse the Matrix recursively.'''

def printMatrix(mat):
    m = len(mat)
    n = len(mat[0])
    # print it
    for i in range(m):
        for j in range(n):
            print(mat[i][j],end = " ")
        print("\n")
        
mat = [[1,2,3],[4,5,6],[7,8,9]]
printMatrix(mat)