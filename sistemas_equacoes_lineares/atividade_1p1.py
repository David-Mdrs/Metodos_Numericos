"""
Exercício 1.1 Classifique os sistemas abaixo com relação a quantidade e existência de soluções.

a)
    x + 2y + 3z = 1
    4x + 5y + 6z = 1
    7x + 8y + 9z = 1


b)

    2x + 3y = 10
    -4x - 6y = -10
"""

# Letra a)
import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

b = np.array([1,1,1])

print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(np.c_[A,b]))

# Letra b)

A = np.array([[2,3],
            [-4,-6]])

b = np.array([10,-10])

print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(np.c_[A,b]))