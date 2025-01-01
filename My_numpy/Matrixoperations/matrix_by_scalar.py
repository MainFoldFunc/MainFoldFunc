"""
This function returns a matrix multiplied by a scalr in R
Takes 2 input:
    A matrix wich is a 3d list
    Ant the scalar wich is a float
"""
def matrix_scalar(matrix: list, scalar: float):
    if not matrix_1:
        raise Exception("You can't enter empty matrix")
   for i in range (len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= scalar
