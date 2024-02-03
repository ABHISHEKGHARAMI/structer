# matrix rotation 90 anti clock wise without using the extra space

def matrixRotation90(mat):
    n = len(mat)
    for i in range(n//2):
        j = i
        while j < n - i - 1:
            temp = mat[i][j]
            mat[i][j] = mat[j][n - i -1]
            mat[j][n - i - 1] = mat[n - i - 1][n - j - 1]
            mat[n - i - 1][n - j - 1] = mat[n - j - 1][i]
            mat[n - j - 1][i] = temp
            j+=1
    return mat
    
mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(f"After the matrix rotation the matrix will be : {matrixRotation90(mat)}")
