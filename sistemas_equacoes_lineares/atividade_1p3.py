import numpy as np

"""
Podemos usar a mesma função da questão anterior
mudando apenas algumas linhas para realizar a substituição progressiva
"""

def sist_lin_tri_inf(A, b):

    n = len(b)
    x = np.empty(n)
    x[0] = b[0] / A[0,0]
    print("x[0] =", x[0])

    for i in range(1, n):
        soma = np.sum(A[i,:i] * x[:i])
        x[i] = (b[i] - soma) / A[i,i]
        print("x[", i, "] =", x[i])

    return x


A = np.array([
    [3,0,0,0],
    [2,1,0,0],
    [1,0,1,0],
    [1,1,1,1]
])

b = np.array([4,2,4,2])
x = sist_lin_tri_inf(A, b)

print("\nSolução:")
print(x)