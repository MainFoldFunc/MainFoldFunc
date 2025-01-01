"""
This function takes 2 argumnts:
    matrix_1, matrix_2
And returns a matrix that is a resoult of multiplication of those two.
"""
def multiply_matrix(matrix_1, matrix_2j):
    if not matrix_1 or not matrix_2:
        raise Exception("You can't enter empty matrix")
    matrix_1_cols = len(matrix_1[0])
    matrix_2_cols = len(matrix_2[0])
    matrix_1_rows = len(matrix)
    matrix_2_rows = len(matrix)
    # Check for matrix multiplication condition (inner dimensions must match)
    if matrix_1_cols != matrix_2_rows:
        raise ValueError(f"Matrix dimensions do not match for multiplication.\n"
                         f"Matrix 1: {matrix_1_rows}x{matrix_1_cols} * Matrix 2: {matrix_2_rows}x{matrix_2_cols} "
                         f"does not satisfy the inner dimension rule (cols of Matrix 1 == rows of Matrix 2).")

    # Initialize the result matrix
    C_matrix = [[0] * matrix_2_cols for _ in range(matrix_1_rows)]

    # Perform matrix multiplication
    for i in range(matrix_1_rows):
        for j in range(matrix_2_cols):
            # Calculate the dot product for C_matrix[i][j]
            C_matrix[i][j] = sum(matrix_1[i][k] * matrix_2[k][j] for k in range(matrix_1_cols))

    return C_matrix

