import numpy as np
import matplotlib.pyplot as plt

matriz_c = np.arange(100).reshape(10, 10)

submatriz_c1 = matriz_c[0:5, 0:5]

print(f"Formato da matriz original C: {matriz_c.shape}")
print(f"Formato da submatriz C1:      {submatriz_c1.shape}")
print("\nSubmatriz:")
print(submatriz_c1)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(matriz_c, cmap='viridis')
ax[0].set_title('Matriz Original C')

ax[1].imshow(submatriz_c1)
ax[1].set_title('Submatriz C1 (5x5)')

plt.show()