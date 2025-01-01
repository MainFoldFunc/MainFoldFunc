"""
Check if matrix is an identity matrix
here is more information:
    https://en.wikipedia.org/wiki/Identity_matrix

function returns a bool
"""
def identity_check(matrix: list) -> bool:
    if not matrix:
        raise Exception("You can't pass an empty matrix")

    # Check if the matrix is square
    rows = len(matrix)
    for row in matrix:
        if len(row) != rows:
            return False

    # Check identity matrix conditions
    for i in range(rows):
        for j in range(rows):
            if i == j:  # Diagonal elements must be 1
                if matrix[i][j] != 1:
                    return False
            else:  # Off-diagonal elements must be 0
                if matrix[i][j] != 0:
                    return False

    return True
