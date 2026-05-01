import numpy as np

def soma_matrizes_manual(matriz_A, matriz_B):

    if matriz_A.shape != matriz_B.shape:
        return "ERRO: Matrizes com tamanhos diferentes não podem ser somadas!"

    # Inicializando a matriz de zeros
    linhas, colunas = matriz_A.shape
    matriz_soma = np.zeros((linhas, colunas))

    # Somando elementos das matrizes
    for i in range(linhas):
        for j in range(colunas):
            matriz_soma[i, j] = matriz_A[i, j] + matriz_B[i, j]
            
    return matriz_soma

# Tamanhos iguais
matriz_A = np.array([[2, 3, 4], [1, 2, 4]])
matriz_B = np.array([[0, 3, 1], [-1, -4, 2]])

print("Soma Correta:\n", soma_matrizes_manual(matriz_A, matriz_B))

# Tamanhos diferentes
matriz_C = np.array([[1, 2], [3, 4]])
print("\nTentativa com tamanhos diferentes:\n", soma_matrizes_manual(matriz_A, matriz_C))