import atv_01 as pf
import numpy as np

"""
Questão 02:

Use a iteração de ponto fixo simples para localizar a raiz de
    f(x) = 2sin(sqrt(x))-x
tendo x0 = 0,5
adotando como critério de parada o erro ≤ 0,001%.
"""

def funcao(x):
    return 2 * np.sin(np.sqrt(x))

x0 = 0.5
tolerancia = 0.001 / 100

pontoFixo, iteracoes = pf.ponto_fixo(funcao, x0, tolerancia)
print("Aproximação do ponto fixo: ", pontoFixo)
print("Iterações: ", iteracoes)