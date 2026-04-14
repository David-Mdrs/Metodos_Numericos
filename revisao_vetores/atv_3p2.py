import numpy as np

def combinacao_linear(lista_escalares, lista_vetores):

    # Garantindo que temos um escalar para cada vetor
    if len(lista_escalares) != len(lista_vetores):
        print("Erro: A quantidade de escalares e vetores deve ser igual.")
        return None

    # Descobrindo o número de dimensões (tamanho) dos vetores
    n_dimensoes = len(lista_vetores[0])
    
    # Criando o molde com vetor nulo
    vetor_resultado = np.zeros(n_dimensoes)

    for i in range(len(lista_escalares)):
        vetor_resultado += lista_escalares[i] * lista_vetores[i]

    return vetor_resultado



"""
Reutilizando a funçao da questão anterior
"""

print("Teste 01: Dimensões Incompatíveis\n")

escalares_a = [2, 3]
vetores_a = [np.array([1, 1, 1]), np.array([1, 1, 1, 1])] 
res_a = combinacao_linear(escalares_a, vetores_a)
print(f"Resultado: {res_a}\n")


print("Teste 02: Quantidades Incompatíveis\n")

escalares_b = [2, 3, 4, 5]
vetores_b = [np.array([1, 1]), np.array([1, 1])]
res_b = combinacao_linear(escalares_b, vetores_b)
print(f"Resultado: {res_b}")


"""
O erro ocorreu porque os dados de entrada são estruturalmente incompatíveis.
Vetores com tamanhos diferentes não podem ser somados
e listas com tamanhos diferentes causariam erro de índice no loop.
"""