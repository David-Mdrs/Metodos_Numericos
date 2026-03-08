import numpy as np

def estimar_pi(k: np.int32):
    n: np.float64 = 0

    for i in range(k):
        n += 4 * (-1)**i * 1 / (2*i + 1)

    return n

termos = np.int32(input("Digite o número de termos: "))
print("Valor estimado de pi: ", estimar_pi(termos))