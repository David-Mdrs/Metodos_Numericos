import numpy as np

def bisection_root(tolerance, function, a, b):

    quite = (a + b) / 2
    f_a = function(a)
    f_quite = function((a + b) / 2)
    f_b = function(b)

    # Condição de parada
    if abs(b - a) < tolerance:
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
Exemplo do material textual: f(x) = 2 - e^x, no intervalo [0, 1]
"""
tolerance = 1
print(f"Para uma tolerância de {tolerance * 100}% a raiz é aproximadamente: "
      , bisection_root(tolerance, lambda x: 2 - np.e**x, 0, 1))
