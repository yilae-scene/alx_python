
# a function that prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            if column !=row[-1] :
                print("{:d}".format(column), end=' ')
            else:
                print("{:d}".format(column), end ='')
        print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
##
print_matrix_integer(matrix)
