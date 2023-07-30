
# define a function that prints the square of a matrix.and returns the new matrix.
#using a list comprhension
def square_matrix_simple(matrix=[[]]):
    new_matrix = [[matrix[i][j]**2 
                    for j in range(len(matrix[i]))] 
                    for i in range (len(matrix)) ]
    return new_matrix



