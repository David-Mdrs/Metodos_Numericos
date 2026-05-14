import numpy as np

def resolver_sistema(A, b):

    # verifica se é diagonal
    if np.all(A == np.diag(np.diagonal(A))):
        print("Matriz diagonal")
        return b / A.diagonal()

    # verifica se é triangular superior
    elif np.all(A == np.triu(A)):
        print("Matriz triangular superior")
        n = len(b)
        x = np.empty(n)
        x[-1] = b[-1] / A[-1,-1]

        for i in range(n-2, -1, -1):
            x[i] = (b[i] - np.sum(A[i,i+1:] * x[i+1:])) / A[i,i]
        return x

    # verifica se é triangular inferior
    elif np.all(A == np.tril(A)):
        print("Matriz triangular inferior")
        n = len(b)
        x = np.empty(n)
        x[0] = b[0] / A[0,0]

        for i in range(1, n):
            x[i] = (b[i] - np.sum(A[i,:i] * x[:i])) / A[i,i]
        return x

    else:
        print("A matriz não é diagonal nem triangular")



# exemplo

A = np.array([
    [3,4,-5,1],
    [0,1,1,-2],
    [0,0,4,-5],
    [0,0,0,2]
])

b = np.array([-10,-1,3,2])
x = resolver_sistema(A, b)

print("\nSolução:")
print(x)