import numpy as np
import matplotlib.pyplot as plt

# Plotando a função para visualizar as raízes
def graph():
    x = np.linspace(-4, 8, 100)
    y = -0.5 * x**2 + 2.5 * x + 4.5

    plt.plot(x, y)
    plt.plot([-1.4, 6.4], [0, 0], 'ro') 
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid()
    plt.show()

def quadratic_function():
    a = -0.5
    b = 2.5
    c = 4.5

    delta = b**2 - 4*a*c

    r1 = (-b + np.sqrt(delta)) / (2*a)
    r2 = (-b - np.sqrt(delta)) / (2*a)

    return r1, r2

def bisection_root(tolerance, function, a, b, counter=1):
    quite = (a + b) / 2
    f_a = function(a)
    f_quite = function((a + b) / 2)
    f_b = function(b)

    # Condição de parada
    if abs(b - a) < tolerance or counter >= 3:
        return quite

    # Existe uma raiz no intervalo [a, meio]
    if (f_a * f_quite < 0):
        return bisection_root(tolerance, function, a, quite, counter + 1)
    
    # Existe uma raiz no intervalo [meio, b]
    elif (f_quite * f_b < 0):
        return bisection_root(tolerance, function, quite, b, counter + 1)
    
    # Encontrou o ponto de inflexão
    else:
        if function(quite) == 0:
            return quite
        else:
            print("Erro: O Teorema de Bolzano não garante raiz neste intervalo.")
            return None
        
# graph()
# print("As raízes da função quadrática são: ", quadratic_function())

xl = 5
xu = 10
bisection_result = bisection_root(0.01, lambda x: -0.5 * x**2 + 2.5 * x + 4.5, xl, xu)

print(f"Utilizando a função quadrática e o método da bisseção para busca da maior raiz, temos: \n")
print(f"Aproximação função quadrática:   {quadratic_function()[1]}")
print(f"Aproximação com método bisseção: {bisection_result}")