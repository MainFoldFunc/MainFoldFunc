"""
add_matrix function takes two matrices
They must be the same size!
"""

def add_matrix(matrix_1: list, matrix_2: list) -> list:
    if len(matrix_1) or len(matrix_2) <= 0:
        raise Exception ("You can't Add two matrieces that has no value")
    if len(matrix_1) != len(matrix_2) and len(matrix_1[0]) != len(matrix_2[0]):
        raise Exception("You can't add two diffrent matrieces")
    matrix_c = []
    for row1, row2 in zip(matrix_1, matrix_2):  # Pair rows from both matrices
        matrix_temp = []
        for elem1, elem2 in zip(row1, row2):  # Pair elements from the paired rows
            matrix_temp.append(elem1 + elem2)
        matrix_c.append(matrix_temp)
    return matrix_c
def sub_matrix(matrix_1: list, matrix_2: list) -> list:
    if len(matrix_1) or len(matrix_2) <= 0:
        raise Exception ("You can't Add two matrieces that has no value")
    if len(matrix_1) != len(matrix_2) and len(matrix_1[0]) != len(matrix_2[0]):
        raise Exception("You can't add two diffrent matrieces")
    matrix_c = []
    for row1, row2 in zip(matrix_1, matrix_2):  # Pair rows from both matrices
        matrix_temp = []
        for elem1, elem2 in zip(row1, row2):  # Pair elements from the paired rows
            matrix_temp.append(elem1 - elem2)
        matrix_c.append(matrix_temp)
    return matrix_c
