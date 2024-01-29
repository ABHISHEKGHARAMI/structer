# determinant for the matrix

def subMatrix(mat,row,col):
    return [
        [mat[i][j] for j in range(len(mat[i])) if j!= col]
        for i in range(len(mat)) if i!= row
    ]
    
    
# determininate matrix
def determinate_Matrix(mat):
    if len(mat) == 1 and len(mat[0]) == 1 :
        return mat[0][0]
    else:
        det = 0
        for j in range(len(mat)):
            det = (-1) ** j * mat[0][j] * determinate_Matrix(subMatrix(mat,0,j))
        return det
    
    
# matrix 
mat = [[2  , 3   ,1 ],[4  , 5   ,7],[6  , 8  , 9]]
print(f"The determinant of the matrix is : {determinate_Matrix(mat)}")