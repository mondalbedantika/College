def input_matrix(name):
    print(f"\n=== {name} ===")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)
    
    return matrix


def print_matrix(matrix, name="Matrix"):
    print(f"\n{name}:")
    for row in matrix:
        print(row)


def add_matrices(mat1, mat2):
    # Check if addition is possible
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same dimensions for addition!")
    
    rows = len(mat1)
    cols = len(mat1[0])
    
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    
    return result

def sub_matrices(mat1,mat2):
    # Check if subtraction is possible
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction!")
    
    rows = len(mat1)
    cols = len(mat1[0])

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(mat1[i][j] - mat2[i][j])
        result.append(row)

    return result

# ==================== Main Program ====================

print("Matrix Addition Program\n")
    
matrix1 = input_matrix("Matrix 1")
print_matrix(matrix1, "Matrix 1")
   
matrix2 = input_matrix("Matrix 2")
print_matrix(matrix2, "Matrix 2")
   
result_add = add_matrices(matrix1, matrix2)
print_matrix(result_add, "Addition Result")

result_sub = sub_matrices(matrix1 , matrix2)
print_matrix(result_sub, "Subtraction Result")
