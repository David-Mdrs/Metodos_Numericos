import numpy as np

def atan_taylor(x, termos):
    soma = 0
    for n in range(termos):
        soma += ((-1)**n * x**(2*n + 1)) / (2*n + 1)
    return soma

pi_real = np.pi
n = 20

# a) Machin
pi_a = 4 * (4 * atan_taylor(1/5, n) - atan_taylor(1/239, n))
# b) Hutton
pi_b = 4 * (atan_taylor(1/2, n) + atan_taylor(1/3, n))
# c) Clausen
pi_c = 4 * (2 * atan_taylor(1/3, n) + atan_taylor(1/7, n))
# d) Dase
pi_d = 4 * (atan_taylor(1/2, n) + atan_taylor(1/5, n) + atan_taylor(1/8, n))

print("Método  | Erro Absoluto")
print("-" * 25)
print("Machin  |", abs(pi_real - pi_a))
print("Hutton  |", abs(pi_real - pi_b))
print("Clausen |", abs(pi_real - pi_c))
print("Dase    |", abs(pi_real - pi_d))

"""
O método de Machin é o melhor porque usa valores menores (1/5 e 1/239). 
Quanto menor o número dentro do arctan, mais rápido a série de Taylor 
chega no valor correto.
"""