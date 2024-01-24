'''

The Matrix rotation for clockwise and anticlockwise rotation.

'''
# first clock wise 90 rotation
def clockwiseMatrix(mat):
    m = len(mat)
    n = len(mat[0])
    # step 1. Transpose the matrix
    transpose_Matrix = [list(row) for row in zip(*mat)]
    
    # step 2: reverse the transpose matrix
    clockMatrix = [list(reversed(row)) for row in transpose_Matrix]
    
    return clockMatrix


# second the anti clock rotation 90' for the matrix
def anticlockwiseMatrix(mat):
    # step 1 : transpose the matrix
    transpose_Matrix = [list(row) for row in (mat)]
    # step 2 : reverse the matrix
    anticlockMatrix = [list(reversed(row)) for row in transpose_Matrix]
    
    return anticlockMatrix


mat = [[1,2,3],[4,5,6],[7,8,9]]
print(f"After the 90' clock wise rotation the matrix will be : {clockwiseMatrix(mat)}")

print(f"After the 90' anticlockwise  rotation the matrix will be : {anticlockwiseMatrix(mat)}")