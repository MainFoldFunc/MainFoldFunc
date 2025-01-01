"""
transposition function takes a one matrix and transposes it more about this here:
    https://en.wikipedia.org/wiki/Transpose
"""
def transposition(matrix: list) -> list:
    if not matrix:  # Check for an empty matrix
        raise Exception("You can't transpose an empty matrix")
    
    # Initialize transposed matrix with correct dimensions
    ret_matrix = [[None] * len(matrix) for _ in range(len(matrix[0]))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            ret_matrix[j][i] = matrix[i][j]
    
    return ret_matrix

