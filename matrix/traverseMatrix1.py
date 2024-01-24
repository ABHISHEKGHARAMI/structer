'''Traverse the Matrix recursively.'''

def printMatrix(mat):
    m = len(mat)
    n = len(mat[0])
    # print it
    for i in range(m):
        for j in range(n):
            print(mat[i][j],end = " ")
        print("\n")


# recursive solving for the matrix

def recursiveMatrix(mat,i,j):
    M = len(mat)
    N = len(mat[0])
    
    # recursion
    if i == M and j == N :
        print(mat[i][j],end=" ")
        return 
    # print the matrix
    print(mat[i][j],end = " ")
    
    # here goes the matrix
    if j < N - 1:
        recursiveMatrix(mat, i , j + 1)
    elif i < M - 1:
        recursiveMatrix(mat, i + 1 ,0)
        


mat = [[1,2,3],[4,5,6],[7,8,9]]
printMatrix(mat)

# after the recursive matrix 
recursiveMatrix(mat , 0 , 0)
# print the matrix
print(f"After recursion the traverse is : {mat}")