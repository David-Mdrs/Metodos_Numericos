import numpy as np

def bisection_root(tolerance, function, a, b):

    quite = (a + b) / 2
    f_a = function(a)
    f_quite = function((a + b) / 2)
    f_b = function(b)

    erro_atual = (abs(b - a) / abs(quite)) * 100
    print(f"Raiz aproximada (X = 0): {quite:.5f} | Erro atual: {erro_atual:.2f}%")

    # Condição de parada
    if erro_atual < (tolerance * 100):
        return quite

    # Existe uma raiz no intervalo [a, meio]
    if (f_a * f_quite < 0):
        return bisection_root(tolerance, function, a, quite)
    
    # Existe uma raiz no intervalo [meio, b]
    elif (f_quite * f_b < 0):
        return bisection_root(tolerance, function, quite, b)
    
    # Encontrou o ponto de inflexão
    else:
        if function(quite) == 0:
            return quite
        else:
            print("Erro: O Teorema de Bolzano não garante raiz neste intervalo.")
            return None
        
"""
Para a função:
f(x) = -2x^6 - 1.5x^4 + 10x + 20
temos que:
f'(x) = -12x^5 - 6x^3 + 10
"""

tolerance = 0.05
equation = lambda x: -12*x**5 - 6*x**3 + 10

a = 0
b = 1

resultado = bisection_root(tolerance, equation, a, b)

print(f"\nPara um erro inferior a {tolerance * 100}%.\nTemos o máximo da função f(x) em aproximadamente:\nX = {resultado}")