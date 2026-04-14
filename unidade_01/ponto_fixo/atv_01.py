"""
Questão 01:

Implemente o algoritmo da iteração de ponto fixo
usando somente a biblioteca Numpy.
"""

def ponto_fixo(funcao, x0, tolerancia, maximo_interacoes=100):
    x_ant = x0
    x_atual = funcao(x0)

    contador = 0
    while abs(x_atual - x_ant) > tolerancia and contador < maximo_interacoes:
        x_ant = x_atual
        x_atual = funcao(x_atual)
        contador += 1

    return x_atual, contador

"""
Com essa função, podemos enviar:
    A função que queremos encontrar o ponto fixo.
    Um chute inicial.
    A tolerância e o número máximo de iterações.
O método irá iterar até encontrar um ponto fixo dentro da tolerância
ou atingir o número máximo de iterações.
"""