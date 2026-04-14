import numpy as np
import matplotlib.pyplot as plt

def graph():
    x_grafico = np.linspace(0, 1.5, 100)
    y_grafico = np.sin(x_grafico) - x_grafico**3

    plt.figure(figsize=(8, 4))
    plt.plot(x_grafico, y_grafico, label="f(x) = sin(x) - x³", color="blue")
    plt.axhline(0, color='black')
    plt.axvline(0.5, color='red', linestyle='--', label="Início do Intervalo (0.5)")
    plt.axvline(1.0, color='green', linestyle='--', label="Fim do Intervalo (1.0)")
    plt.title("Técnica Gráfica: sin(x) = x³")
    plt.grid()
    plt.legend()
    plt.show()

def bisection_root(tolerance, function, a, b):

    quite = (a + b) / 2
    f_a = function(a)
    f_quite = function((a + b) / 2)
    f_b = function(b)

    erro_atual = (abs(b - a) / abs(quite)) * 100
    print(f"Raiz aproximada: {quite:.5f} | Erro atual: {erro_atual:.2f}%")

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


# graph()

tolerance = 0.02
equation = lambda x: np.sin(x) - x**3

a = 0.5
b = 1

resultado = bisection_root(tolerance, equation, a, b)

print(f"\nPara um erro inferior a {tolerance * 100}% a raiz não-trivial é aproximadamente: {resultado}")