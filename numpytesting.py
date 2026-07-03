import numpy 

print("Matrix A")
matrix_a = numpy.array([[1, 2], [3, 4]])
print(matrix_a)

print("Matrix B")
matrix_b = numpy.array([[5, 6], [7, 8]])
print(matrix_b)

print("Dot Product")
dot_product = numpy.dot(matrix_a, matrix_b)
print(dot_product)

print("Transpose")
matrix_transpose = numpy.transpose(matrix_a)
print(matrix_transpose)
