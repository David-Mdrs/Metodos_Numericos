import numpy as np
import matplotlib.pyplot as plt

matriz_c = np.arange(100).reshape(10, 10)


# T - topo
# B - base
# L - esquerda
# R - direita

bloco_TE = matriz_c[0:5, 0:5]   # Linhas 0-5, Colunas 0-5
bloco_TD = matriz_c[0:5, 5:10]  # Linhas 0-5, Colunas 5-10
bloco_BE = matriz_c[5:10, 0:5]  # Linhas 5-10, Colunas 0-5
bloco_BD = matriz_c[5:10, 5:10] # Linhas 5-10, Colunas 5-10

# Reorganizando os blocos
topo = np.hstack((bloco_BD, bloco_BE))
base = np.hstack((bloco_TD, bloco_TE))

# Juntar as duas metades verticalmente
matriz_c_reorganizada = np.vstack((topo, base))


# Criando figura com as duas matrizes
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].imshow(matriz_c, cmap='gray')
ax[0].set_title('Matriz Original C')

ax[1].imshow(matriz_c_reorganizada, cmap='gray')
ax[1].set_title('Matriz Reorganizada (Ex. 5-3)')

plt.show()


print("Matriz Reorganizada:\n")
print(matriz_c_reorganizada)