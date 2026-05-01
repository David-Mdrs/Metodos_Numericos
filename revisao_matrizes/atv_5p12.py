import numpy as np

# Matrizes diagonais 3x3
matriz_diagonal_A = np.diag([1, 2, 3])
matriz_diagonal_B = np.diag([4, 5, 6])

# Multiplicando matriz padrão
resultado_padrao = matriz_diagonal_A @ matriz_diagonal_B

# Multiplicação de Hadamard
resultado_hadamard = matriz_diagonal_A * matriz_diagonal_B



diferenca_maxima = np.max(np.abs(resultado_padrao - resultado_hadamard))
sao_iguais = diferenca_maxima < 1e-15

print("Resultado com @ (Padrão):")
print(resultado_padrao)

print("\nResultado com * (Hadamard):")
print(resultado_hadamard)

print("\nResultados iguais: ", sao_iguais)