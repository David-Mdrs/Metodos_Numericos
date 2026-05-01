import numpy as np

# 1. Definindo as dimensões
linhas_A  = 4
comum     = 3  # Colunas de A e linhas de B iguais
colunas_B = 5

matriz_A = np.random.randn(linhas_A, comum)
matriz_B = np.random.randn(comum, colunas_B)

matriz_resultado_manual = np.zeros((linhas_A, colunas_B))

for i in range(linhas_A):
    for j in range(colunas_B):
        
        for k in range(comum):
            matriz_resultado_manual[i, j] += matriz_A[i, k] * matriz_B[k, j]

# Verificando usando o operador @
matriz_resultado_numpy = matriz_A @ matriz_B

sao_iguais = np.allclose(matriz_resultado_manual, matriz_resultado_numpy)

print("Matriz A: ", matriz_A.shape)
print("Matriz B: ", matriz_B.shape)
print("Resultado Manual: ", matriz_resultado_manual.shape)

print("\nResultado da igualdade: ", sao_iguais)