import numpy as np

def funcao_01(mu):
    return np.exp(1/mu) / (1 + np.exp(1/mu))

def funcao_02(mu):
    return 1 / (1 + np.exp(-1/mu))

print("mu | f1(mu) | f2(mu)")

for i in range(1, 10):
    mu = 1 / (10 ** i)
    f1 = funcao_01(mu)
    f2 = funcao_02(mu)
    print(mu, " | ", f1, " | ", f2)

"""
A primeira fórmula é perigosa porque tenta calcular 
um número absurdamente grande ($e$ elevado a mil), 
chegando a um overflow.

A segunda fórmula é inteligente porque transforma
o problema em um número quase zero ($e$ elevado a menos mil).
O computador lida muito melhor com o "quase nada" do que com o "infinito".
"""