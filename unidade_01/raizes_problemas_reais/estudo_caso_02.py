# Estudo de Caso 2 - Equilíbrio de mercado

import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

""" CURVA DE DEMANDA """
def modelo_preco_demanda(P, a, b):
    return a - b * np.log(P)

def curva_preco_demanda():
    dados = pd.read_csv(r'raizes_problemas_reais\coffee_market_dataset.csv')
    x_preco = dados['price_usd'].values
    y_demanda = dados['quantity_demand'].values

    chute = [1.0, 0.1]

    popt, pcov = curve_fit(modelo_preco_demanda, x_preco, y_demanda, p0=chute)
    a_otimizado, b_otimizado = popt
    print(f"Parâmetros: a={a_otimizado:.4f}, b={b_otimizado:.4f}")

    plt.scatter(x_preco, y_demanda)
    x_ord = np.sort(x_preco) 
    plt.plot(x_ord, modelo_preco_demanda(x_ord, *popt), color='red')
    plt.xlabel('Preço (USD)')
    plt.ylabel('Demanda')
    plt.title('Relação entre Preço e Demanda')
    plt.show()


""" CURVA DE OFERTA """
def modelo_preco_oferta(P, c, d):
    return c * np.exp(d * P)

def curva_preco_oferta():
    dados = pd.read_csv(r'raizes_problemas_reais\coffee_market_dataset.csv')
    x_preco = dados['price_usd'].values
    y_oferta = dados['quantity_supply'].values

    chute = [1.0, 0.1]

    popt, pcov = curve_fit(modelo_preco_oferta, x_preco, y_oferta, p0=chute)
    a_otimizado, b_otimizado = popt
    print(f"Parâmetros: a={a_otimizado:.4f}, b={b_otimizado:.4f}")

    plt.scatter(x_preco, y_oferta)
    x_ord = np.sort(x_preco) 
    plt.plot(x_ord, modelo_preco_oferta(x_ord, *popt), color='red')
    plt.xlabel('Preço (USD)')
    plt.ylabel('Oferta')
    plt.title('Relação entre Preço e Oferta')
    plt.show()


""" PREÇO E EQUILÍBRIO"""
def modelo_equilibrio(P, a, b, c, d): 
    return (a - b * np.log(P)) - (c * np.exp(d * P))

def curva_preco_equilibrio():
    dados = pd.read_csv(r'raizes_problemas_reais\coffee_market_dataset.csv')
    preco = dados['price_usd'].values
    demanda = dados['quantity_demand'].values
    oferta = dados['quantity_supply'].values

    diferenca = demanda - oferta

    chute = [10.0, 1.0, 1.0, 0.01]

    popt, pcov = curve_fit(modelo_equilibrio, preco, diferenca, p0=chute, maxfev=10000, bounds=(0, np.inf))
    a_otimizado, b_otimizado, c_otimizado, d_otimizado = popt
    
    print(f"Parâmetros encontrados:")
    print(f"a={a_otimizado:.4f}, b={b_otimizado:.4f}, c={c_otimizado:.4f}, d={d_otimizado:.4f}")

    plt.figure(figsize=(8, 6))
    plt.scatter(preco, diferenca, color='blue', alpha=0.6, label='Dados reais (Demanda - Oferta)')

    limite_estendido = max(preco) + 15
    x_continuo = np.linspace(min(preco), limite_estendido, 100) 
    plt.plot(x_continuo, modelo_equilibrio(x_continuo, *popt), color='red', linewidth=2, label='Curva Ajustada')

    plt.axhline(0, color='black', linestyle='--', label='Equilíbrio (Y = 0)')

    plt.xlabel('Preço (USD)')
    plt.ylabel('Diferença (Demanda - Oferta)')
    plt.title('Buscando o Preço de Equilíbrio do Café')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
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


""" CURVA DE DEMANDA """
# curva_preco_demanda()

""" CURVA DE OFERTA """
# curva_preco_oferta()

""" PREÇO E EQUILÍBRIO """
# curva_preco_equilibrio()

"""
Visualmente, percebemos que a raiz toca o eixo X entre o intervalo [20, 25].
Sabendo também que os parâmetros otimizados foram: a=120.2965, b=15.0312, c=5.1468, d=0.1182.
Podemos usar o método de bisseção para a função: f(P) = (120.2965 - 15.0312 * np.log(P)) - (5.1468 * np.exp(0.1182 * P))
"""

tolerancia = 0.05
equacao = lambda P: (120.2965 - 15.0312 * np.log(P)) - (5.1468 * np.exp(0.1182 * P))

a = 20
b = 25

resultado = metodo_bissecao(tolerancia, equacao, a, b)
print(f"\nResultado final: P = {resultado}")