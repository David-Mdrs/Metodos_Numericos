# Estudo de Caso 1 - Evapora ̧cão e temperatura

import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


""" EXPLORAÇÃO DE DADOS """
def grafico_dispersao():
    dados = pd.read_csv(r'raizes_problemas_reais\climate_evaporation_dataset.csv')
    dados.plot.scatter(x='temperature_c', y='evaporation_mm_day')
    plt.title('Relação entre Temperatura e Evaporação')
    plt.show()


""" MODELAGEM """
def modelo(T, a, b):
    return a * np.exp(b * T)

def ajuste_curva():
    dados = pd.read_csv(r'raizes_problemas_reais\climate_evaporation_dataset.csv')
    dados.head()
    x_temperatura = dados['temperature_c'].values
    y_evaporacao = dados['evaporation_mm_day'].values

    chute = [1.0, 0.1]

    popt, pcov = curve_fit(modelo, x_temperatura, y_evaporacao, p0=chute)
    a_otimizado, b_otimizado = popt
    print(f"Parâmetros: a={a_otimizado:.4f}, b={b_otimizado:.4f}")

    plt.scatter(x_temperatura, y_evaporacao)
    x_ord = np.sort(x_temperatura) 
    plt.plot(x_ord, modelo(x_ord, *popt), color='red')
    plt.show()


""" PROBLEMA DE RAIZ """
def modelo_raiz(T, a, b):
    return (a * np.exp(b * T)) - 5
    
def encontrar_raiz():
    dados = pd.read_csv(r'raizes_problemas_reais\climate_evaporation_dataset.csv')
    dados.head()
    x_temperatura = dados['temperature_c'].values
    y_evaporacao = dados['evaporation_mm_day'].values

    chute = [1.0, 0.1]

    popt, pcov = curve_fit(modelo, x_temperatura, y_evaporacao, p0=chute)
    a_otimizado, b_otimizado = popt
    print(f"Parâmetros: a={a_otimizado:.4f}, b={b_otimizado:.4f}")

    plt.scatter(x_temperatura, y_evaporacao)
    x_ord = np.sort(x_temperatura) 
    plt.plot(x_ord, modelo_raiz(x_ord, *popt), color='red')
    plt.show()

def metodo_bissecao(tolerancia, funcao, a, b):
    # Função desenvolvida nas atividades anteriores

    meio = (a + b) / 2
    f_a = funcao(a)
    f_meio = funcao((a + b) / 2)
    f_b = funcao(b)

    erro_atual = (abs(b - a) / abs(meio)) * 100
    print(f"Raiz aproximada: {meio:.5f} | Erro atual: {erro_atual:.2f}%")

    # Condição de parada
    if abs(b - a) < tolerancia:
        return meio

    # Existe uma raiz no intervalo [a, meio]
    if (f_a * f_meio < 0):
        return metodo_bissecao(tolerancia, funcao, a, meio)
    
    # Existe uma raiz no intervalo [meio, b]
    elif (f_meio * f_b < 0):
        return metodo_bissecao(tolerancia, funcao, meio, b)
    
    # Encontrou o ponto de inflexão
    else:
        if funcao(meio) == 0:
            return meio
        else:
            print("Erro: O Teorema de Bolzano não garante raiz neste intervalo.")
            return 
        



""" EXPLORAÇÃO DE DADOS """
# grafico_dispersao()

""" MODELAGEM """
# ajuste_curva()

""" PROBLEMA DE RAIZ """
# encontrar_raiz()

"""
Visualmente, percebemos que a raiz toca o eixo X entre o intervalo [30, 35].
Sabendo também que os parâmetros otimizados foram: a=0.3871 e b=0.0809.
Podemos usar o método de bisseção para a função: f(T) = (0.3871 * exp(0.0809 * T)) - 5
"""

tolerancia = 0.05
equacao = lambda T: (0.3871 * np.exp(0.0809 * T)) - 5

a = 30
b = 35

resultado = metodo_bissecao(tolerancia, equacao, a, b)
print(f"\nResultado final: T = {resultado}")