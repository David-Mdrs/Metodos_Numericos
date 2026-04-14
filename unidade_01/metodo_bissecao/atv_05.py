def falsa_posicao(tolerancia, funcao, a, b):

    erro_atual = float('inf')
    palpite_anterior = None
    while(erro_atual > tolerancia * 100):

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
            print(f"Palpite para raiz (X = 0): {palpite:.5f} | Erro atual: {erro_atual:.2f}%")

        palpite_anterior = palpite

    return palpite

"""
Usando a mesma função do exercício 4 (atv_04.py).
Cujo resultado foi X = 0.859375.
Calculamos usando o método da falsa posição:
"""

tolerancia = 0.05
equacao = lambda x: -12*x**5 - 6*x**3 + 10

a = 0
b = 1

resultado = falsa_posicao(tolerancia, equacao, a, b)
print(f"\nResultado final: X = {resultado}")

"""
Por fim, podemos concluir que o método da "falsa posição"
é realmente mais eficiente, pois, para a mesma tolerância (5%),
obteve-se um resultado mais próximo do valor real (X = 0.859375) em apenas 3 iterações,
enquanto o método da bisseção (atv_04.py) levou 6 iterações para alcançar o mesmo nível de precisão.
"""