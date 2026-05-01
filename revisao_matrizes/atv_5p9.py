import numpy as np

# Matriz quadrada aleatória
matriz_A = np.random.randn(4, 4)

matriz_S = (matriz_A + matriz_A.T) / 2

# Confirmando simetria da matriz resultante
distancia_transposta = np.max(np.abs(matriz_S - matriz_S.T))
e_simetrica = distancia_transposta < 1e-15

print("Simetria da matriz resultante:      ", e_simetrica)
print("Diferença máxima para a transposta: ", distancia_transposta)