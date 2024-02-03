# try to practice for roattion of the matrix clockwise and anticlockwise direction
def anticlockwise(mat):
    m = len(mat)
    n = len(mat[0])
    
    transpose_Matrix = [list(row) for row in zip(*mat)]
    # reverse matrix for the anti clock wise rotation     
    reverse_rotation = transpose_Matrix[::-1]
    
    return reverse_rotation
        

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(f"The anticlockwise rotation of the matrix is : {anticlockwise(mat)}")