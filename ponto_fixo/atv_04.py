"""
Questão 04:

Compare os métodos:
    bisseção;
    falsa posição;
    ponto fixo.
localizando a raiz das seguintes quações:

a) f1(x) = 2x^4 + 4x^3 + 3x^2 - 10x - 15, no intervalo [0, 3].

b) f2(x) = (x + 3)(x + 1)(x - 2)^3, no intervalo [0, 5].

c) f3(x) = 5x^3 + x^2 - e^(1-2x) + cos(x) + 20, no intervalo [-5, 5].

d) f4(x) = sin(x)x + 4, no intervalo [1, 5].

e) f5(x) = (x - 3)^5*ln(x), no intervalo [2, 5].

f) f6(x) = x^10 - 1, no intervalo [0.8, 1.2]
"""

import math

def f1(x):
    return 2*x**4 + 4*x**3 + 3*x**2 - 10*x - 15

def f2(x):
    return (x + 3)*(x + 1)*(x - 2)**3

def f3(x):
    return 5*x**3 + x**2 - math.exp(1-2*x) + math.cos(x) + 20

def f4(x):
    return math.sin(x)*x + 4

def f5(x):
    return (x - 3)**5 * math.log(x)

def f6(x):
    return x**10 - 1



def metodo_bissecao(tolerancia, funcao, a, b):
    if funcao(a) * funcao(b) > 0:
        print("Erro: O Teorema de Bolzano não garante raiz neste intervalo.")
        return None, 0

    contador = 0
    while True:
        contador += 1
        meio = (a + b) / 2
        f_a = funcao(a)
        f_meio = funcao(meio)
        f_b = funcao(b)

        erro_atual = abs(b - a) / 2

        if erro_atual < (tolerancia * 100): 
            return meio, contador
        
        if f_meio == 0:
            return meio, contador
        
        if (f_a * f_meio < 0):
            b = meio
        elif (f_meio * f_b < 0):
            a = meio

def falsa_posicao(tolerancia, funcao, a, b):

    erro_atual = float('inf')
    palpite_anterior = None
    contador = 0
    while(erro_atual > tolerancia * 100):
        contador += 1

        f_a = funcao(a)
        f_b = funcao(b)
        palpite = b - (f_b * (a - b)) / (f_a - f_b)
        valor = funcao(palpite)

        if (f_a * valor < 0):
            b = palpite
        else:
            a = palpite
        
        if palpite_anterior is not None:
            erro_atual = (abs(palpite - palpite_anterior) / abs(palpite)) * 100

        palpite_anterior = palpite

    return palpite, contador

def ponto_fixo(funcao, x0, tolerancia, maximo_interacoes=100):
    x_ant = x0
    x_atual = funcao(x0)

    contador = 0
    while abs(x_atual - x_ant) > tolerancia and contador < maximo_interacoes:
        x_ant = x_atual
        x_atual = funcao(x_atual)
        contador += 1

    return x_atual, contador

def comparar(titulo, f, g, a, b):
    tolerancia = 0.001 / 100
    print(f"\n{titulo}")
    print(f"Intervalo: [{a}, {b}]\n")

    # 1. Bisseção
    raiz_b, iter_b = metodo_bissecao(tolerancia, f, a, b)
    print(f"Bisseção      Raiz: {raiz_b:.5f} | Iterações: {iter_b}")

    # 2. Falsa Posição
    raiz_fp, iter_fp = falsa_posicao(tolerancia, f, a, b)
    print(f"Falsa Posição Raiz: {raiz_fp:.5f} | Iterações: {iter_fp}")

    # 3. Ponto Fixo
    try:
        x0 = (a + b) / 2
        raiz_pf, iter_pf = ponto_fixo(g, x0, tolerancia)
        print(f"Ponto Fixo    Raiz: {raiz_pf:.5f} | Iterações: {iter_pf}")
    except OverflowError:
        print("Ponto Fixo    Falhou: Divergiu")
    except Exception as e:
        print(f"Ponto Fixo    Falhou: {e}")



def f1_comparar():
    g1 = lambda x: (2*x**4 + 4*x**3 + 3*x**2 - 15) / 10
    comparar("Letra A: f1(x) = 2x^4 + 4x^3 + 3x^2 - 10x - 15", f1, g1, 0, 3)

def f2_comparar():
    g2 = lambda x: f2(x) + x
    comparar("Letra B: f2(x) = (x + 3)(x + 1)(x - 2)^3", f2, g2, 0, 5)

def f3_comparar():
    g3 = lambda x: math.sqrt(math.exp(1-2*x) - 5*x**3 - math.cos(x) - 20) if (math.exp(1-2*x) - 5*x**3 - math.cos(x) - 20) >= 0 else 0
    comparar("Letra C: f3(x) = 5x^3 + x^2 - e^(1-2x) + cos(x) + 20", f3, g3, -5, 5)

def f4_comparar():
    g4 = lambda x: -4 / math.sin(x) if math.sin(x) != 0 else 0
    comparar("Letra D: f4(x) = sin(x)*x + 4", f4, g4, 1, 5)

def f5_comparar():
    g5 = lambda x: x - f5(x) if x > 0 else 0.1
    comparar("Letra E: f5(x) = (x - 3)^5 * ln(x)", f5, g5, 2, 5)

def f6_comparar():
    g6 = lambda x: 1 / (x**9) if x != 0 else 0
    comparar("Letra F: f6(x) = x^10 - 1", f6, g6, 0.8, 1.2)



""" COMPARANDO MODELOS E FUNÇÕES """
# f1_comparar()
# f2_comparar()
# f3_comparar()
# f4_comparar()
# f5_comparar()
# f6_comparar()