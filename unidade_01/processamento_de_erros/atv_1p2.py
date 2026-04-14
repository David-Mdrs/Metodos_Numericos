import numpy as np

e = 1.0
epsilon_numpy = np.finfo(float).eps

while (1.0 + e) > 1.0:
    print("Valor atual de e: ", e)
    e = e / 2.0

epsilon_calculado = 2.0 * e

print("\nÉpsilon calculado: ",epsilon_calculado)
print("Épsilon do NumPy:  ", epsilon_numpy)