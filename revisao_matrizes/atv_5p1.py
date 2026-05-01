import numpy as np

matriz = np.arange(12).reshape(3, 4)

linha = 1 
coluna = 3

elemento = matriz[linha, coluna]

print("Matriz criada:\n")
print(matriz, "\n")

print(f"O elemento da matriz no índice ({linha + 1},{coluna + 1}) é {elemento}.")