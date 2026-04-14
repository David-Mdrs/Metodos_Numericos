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



escalares = [2, -3, 4]
vetores = [
    np.array([1, 2, 0]),
    np.array([-1, 0, 3]),
    np.array([3, 1, -1])
]


resultado_final = combinacao_linear(escalares, vetores)

print("Combinação Linear Ponderada\n")

print(f"Escalares: {escalares}")
print(f"Vetores:   {vetores}")
print(f"Resultado: {resultado_final}")