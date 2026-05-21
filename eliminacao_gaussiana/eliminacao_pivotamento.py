import numpy as np

"""
Usando o notebook disponível
podemos usar como base para nossa função.
"""

def eliminacao_gaussiana_pivotamento(A, b):

    # Matriz estendida
    A_b = np.c_[A.astype(float), b.astype(float)]

    n = len(b)

    # Eliminação
    for c in range(n - 1):

        # Escolhendo o pivô (maior valor absoluto da coluna)
        p = np.abs(A_b[c:, c]).argmax() + c

        # Trocando de linhas
        A_b[[c, p]] = A_b[[p, c]]

        # Zerando elementos abaixo do pivô
        for i in range(c + 1, n):

            fator = A_b[i, c] / A_b[c, c]

            A_b[i] = A_b[i] - fator * A_b[c]

    # Separando matriz e vetor
    A_tri = A_b[:, :-1]
    b_tri = A_b[:, -1]

    # Substituição regressiva
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):

        soma = 0

        for j in range(i + 1, n):
            soma += A_tri[i, j] * x[j]

        x[i] = (b_tri[i] - soma) / A_tri[i, i]

    return x

A = np.array([
    [2, 3, -1],
    [4, 4, -3],
    [2, -3, 1]
])

b = np.array([5, 3, -1])

x = eliminacao_gaussiana_pivotamento(A, b)

print(x)