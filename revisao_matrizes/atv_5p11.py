import numpy as np

# Criando a matriz cheia de números 1
matriz_A = np.ones((4, 4))

# Criando a matriz diagonal com os valores: 1, 4, 9, 16
valores_diagonal = [1, 4, 9, 16]
matriz_B = np.diag(valores_diagonal)

# Criando a matriz diagonal com a raiz quadrada (1, 2, 3, 4)
matriz_C = np.diag(np.sqrt(valores_diagonal))



# Pré-multiplicar matriz_B na esquerda
resultado_linhas = matriz_B @ matriz_A

# Pós-multiplicar matriz_B na direita
resultado_colunas = matriz_A @ matriz_B

# Multiplicar dos dois lados
matriz_tabuada = matriz_C @ matriz_A @ matriz_C


print("Escalando as LINHAS (1, 4, 9, 16):")
print(resultado_linhas)

print("\nEscalando as COLUNAS (1, 4, 9, 16):")
print(resultado_colunas)

print("\nResultado da Tabuada (1x1, 2x2, 3x3, 4x4...):")
print(matriz_tabuada)