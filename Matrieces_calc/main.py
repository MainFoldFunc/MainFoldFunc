

def how_to_make_matrix():
    print("First say what parameters should the matrix have")
    print("The parameters are like this:")
    print("|\\ | [[x1, x2],")
    print("| \\|  [x3, x4]]")
    print("           *    ")
    print("           |    ") 
    print("           |    ")   

def matrix_from_user() -> list, int, int:
    how_to_make_matrix()

    rows = int(input("How many rows has this matrix"))
    cols = int(input("How many cols has this matrix"))

    matrix = []
    for i in range(cols):
        row_list = []
        for j in range(rows):
            xi = int(input(f"What is the {j} elemnt of this row: "))
            row_list.append(xi)
        matrix.append(row_list)

    return matrix, rows, cols

func main ():
    matrix_1, matrix_1_rows, matrix_1_cols = matrix_from_user()
    matrix_2, matrix_2_rows, matrix_2_cols = matrix_from_user()

    if matrix_1_rows == matrix_2_rows:
        multiply_matrix(matrix_1, matrix_2, matrix_1_cols, matrix_2_rows)
    else:
        print(f"You cant multiply two matireces ({matrix_1_cols}x{matrix_1_rows}) by a ({matrix_2_cols}x{matrix_2_rows})")
        print("Inner dimensions are not the same")
