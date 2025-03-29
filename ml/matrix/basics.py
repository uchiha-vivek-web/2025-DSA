""" Creating a matrix """
import numpy as np

matrix_1= np.array([[1,2],[3,4]])
print(f"shape:{matrix_1.shape}")
print(matrix_1)

matrix_2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"shape:{matrix_2.shape}")
print(matrix_2)

""" create a matrix with random values """
random_matrix  = np.random.rand(3,3)
print(random_matrix)

""" create a matrix with random integers """
random_integer_matrix = np.random.randint(10,size=(3,3))
print(random_integer_matrix)

"""matrix with all values as 1"""
matrix_1= np.ones((2,3))
print(matrix_1)
matrix_2 =np.ones((2,3),dtype=int)
print(matrix_2)


""" creating a null matrix """
matrix_1 = np.zeros((2,3))
print(matrix_1)
matrix_2 = np.zeros((2,3),dtype=int)
print(matrix_2)

""" identity matrix """
matrix_1 = np.eye(3,3)
print(matrix_1)


""" Transpose of a matrix """
matrix_1 = np.random.randint(10,size=(3,3))
print(f"Normal matrix : {matrix_1} ")
transpose_of_matrix = np.transpose(matrix_1)
print(f'Transpose of matrix : {transpose_of_matrix}')