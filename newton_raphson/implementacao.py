import numpy as np

"""
Podemos utilizar o método gradient() do numpy para calcular a derivada numérica da função f(x).
"""
def derivada_numerica(funcao, x, h=1e-5):
    return (funcao(x + h) - funcao(x - h)) / (2 * h)


"""
Implementando o método de newton_raphson.

Tendo como base a equação: 
    Xn+1 = Xn - f(Xn) / f'(Xn)
"""
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


"""
Implementando o método da secante.

Tendo como base a equação:
    Xn+1 = Xn - f(Xn) * (Xn - Xn-1) / (f(Xn) - f(Xn-1))
"""
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


"""
Testando ambos os testes.
"""
# print("Exemplo de uso dos métodos de Newton-Raphson e Secante")
# f = lambda x: x**3 - x - 2

# print(newton_raphson(f, 1.5))
# print(secante(f, 1.0, 1.5))