import numpy as np

"""
Tendo como base o exemplo dado no roteiro, podemos ampliar a função para
explicitar cada etapa da substituição retroativa
"""

def sist_lin_tri_sup(A, b):

    n = len(b)
    x = np.empty(n)
    x[-1] = b[-1] / A[-1, -1]
    print("x[3] =", x[-1])

    for i in range(n-2, -1, -1):
        soma = np.sum(A[i, i+1:] * x[i+1:])
        x[i] = (b[i] - soma) / A[i, i]
        print("x[", i, "] =", x[i])

    return x


A = np.array([
    [3, 4, -5, 1],
    [0, 1, 1, -2],
    [0, 0, 4, -5],
    [0, 0, 0, 2]
])

b = np.array([-10, -1, 3, 2])
x = sist_lin_tri_sup(A, b)

print("\nSolução:")
print(x)