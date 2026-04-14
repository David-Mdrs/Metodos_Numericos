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



"""Novos métodos: Newton-Raphson e Secante"""

def derivada_numerica(funcao, x, h=1e-5):
    return (funcao(x + h) - funcao(x - h)) / (2 * h)

def newton_raphson(funcao, x0, tolerancia=1e-5, max_iteracoes=100):
    x = x0

    for i in range(max_iteracoes):
        fx = funcao(x)
        dfx = derivada_numerica(funcao, x)

        if dfx == 0:
            print("Derivada zero, método falhou.")
            return None, i

        x_novo = x - fx / dfx

        if abs(x_novo - x) < tolerancia:
            return x_novo, i

        x = x_novo

    return x, max_iteracoes

def secante(funcao, x0, x1, tolerancia=1e-5, max_iteracoes=100):
    x_ant = x0
    x_atual = x1

    for i in range(max_iteracoes):
        f_ant = funcao(x_ant)
        f_atual = funcao(x_atual)

        if f_atual - f_ant == 0:
            print("Divisão por zero, método falhou.")
            return None, i

        x_prox = x_atual - f_atual * (x_atual - x_ant) / (f_atual - f_ant)

        if abs(x_prox - x_atual) < tolerancia:
            return x_prox, i

        x_ant = x_atual
        x_atual = x_prox

    return x_atual, max_iteracoes



def comparar(titulo, f, g, a, b):
    tolerancia = 0.001 / 100

    print("========== INICIANDO COMPARAÇÃO DE MÉTODOS ==========")
    print(titulo)
    print("Intervalo:", [a, b])
    print()

    # Bisseção
    raiz_b, it_b = metodo_bissecao(tolerancia, f, a, b)
    print("Bisseção -> Raiz:", round(raiz_b, 5), "| Iterações:", it_b)

    # Falsa posição
    raiz_fp, it_fp = falsa_posicao(tolerancia, f, a, b)
    print("Falsa posição -> Raiz:", round(raiz_fp, 5), "| Iterações:", it_fp)

    # Ponto fixo
    x0 = (a + b) / 2
    try:
        raiz_pf, it_pf = ponto_fixo(g, x0, tolerancia)
        print("Ponto fixo -> Raiz:", round(raiz_pf, 5), "| Iterações:", it_pf)
    except Exception:
        print("Ponto fixo -> não convergiu")

    # Newton
    try:
        raiz_nr, it_nr = newton_raphson(f, x0, tolerancia)
        print("Newton -> Raiz:", round(raiz_nr, 5), "| Iterações:", it_nr)
    except Exception:
        print("Newton -> erro")

    # Secante
    try:
        raiz_sec, it_sec = secante(f, a, b, tolerancia)
        print("Secante -> Raiz:", round(raiz_sec, 5), "| Iterações:", it_sec)
    except Exception:
        print("Secante -> erro")

    print("=====================================================\n")




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

"""
O método de Newton-Raphson apresentou a melhor eficiência na maioria dos casos,
enquanto a bisseção se destacou pela robustez.
A falsa posição mostrou baixa eficiência em funções com raízes múltiplas,
e o método do ponto fixo demonstrou forte dependência da escolha da função de iteração, podendo divergir.
A secante apresentou bom desempenho, porém sem garantia de permanência no intervalo inicial.
"""