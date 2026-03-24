"""
Questão 03:

Determine a maior raiz real de
    f(x) = 2x³ - 11.7x² + 17.7x - 5

a) Graficamente;
b) Pelo método da Bisseção (5 iterações, escolha o intervalo pela visualização gráfica);
c) Pelo método da iteração de ponto fixo (5 iterações, x0 = 3).
   Certifique-se de desenvolver uma solução que convirja para a raiz.
"""

import numpy as np
import matplotlib.pyplot as plt

def graph():
    x = np.arange(-2, 2, 0.1)
    y = 2*x**3 - 11.7*x**2 + 17.7*x - 5

    plt.plot(x, y)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid()
    plt.show()

def metodo_bissecao(tolerancia, funcao, a, b):

    meio = (a + b) / 2
    f_a = funcao(a)
    f_meio = funcao(meio)
    f_b = funcao(b)

    erro_atual = abs(b - a) / 2

    if erro_atual < (tolerancia * 100):
        return meio
    
    if (f_a * f_meio < 0):
        return metodo_bissecao(tolerancia, funcao, a, meio)
    
    elif (f_meio * f_b < 0):
        return metodo_bissecao(tolerancia, funcao, meio, b)
    
    else:
        if funcao(meio) == 0:
            return meio
        else:
            print("Erro: O Teorema de Bolzano não garante raiz neste intervalo.")
            return None

def ponto_fixo(funcao, x0, tolerancia, maximo_interacoes=100):
    x_ant = x0
    x_atual = funcao(x0)

    contador = 0
    while abs(x_atual - x_ant) > tolerancia and contador < maximo_interacoes:
        x_ant = x_atual
        x_atual = funcao(x_atual)
        contador += 1

    return x_atual, contador



def funcao(x):
    return (-2*x**3 + 11.7*x**2 + 5) / 17.7

x0 = 3
tolerancia = 0.001 / 100

# graph()

print("Pelo método da Bisseção: ", metodo_bissecao(tolerancia, lambda x: 2*x**3 - 11.7*x**2 + 17.7*x - 5, x0, 5))

print("Pelo método da iteração de ponto fixo: ", ponto_fixo(funcao, x0, tolerancia, 5)[0])
