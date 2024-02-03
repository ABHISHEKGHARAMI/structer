# Nw we have done the matrix rotation for the anticlockwise then have to do the clockwise rotation 
# without using the extra space

def matrixRotation90Clock(mat):
    n = len(mat)
    for i in range(n//2):
        j = i
        while j < n - i - 1:
            temp = mat[i][j]
            mat[i][j] = mat[n -1 - j][i]
            mat[n - 1 - j][i] = mat[n - 1 - i][n - 1 - j]
            mat[n - 1 - i][n - 1 - j] = mat[j][n - i - 1]
            mat[j][n - 1 - i] = temp
            j += 1
    return mat

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(f"After the clock wise 90' rotation the matrix will be : {matrixRotation90Clock(mat)}")
