import matplotlib.pyplot as plt

def plotar_vetores(vetores, titulo = "Gráfico de Vetores"):
    """
    Deve-se passar uma lista de vetores, passando as coordenadas iniciais e finais no seguinte formato:
        [[x1, y1], [x2, y2]]...
    """

    # Calculando pontos X e Y de cada vetor
    X = [v[0][0] for v in vetores]
    Y = [v[0][1] for v in vetores]
    
    # Calculando o deslocamento U (horizontal) e V (vertical) de cada vetor
    U = [v[1][0] - v[0][0] for v in vetores]
    V = [v[1][1] - v[0][1] for v in vetores]

    plt.figure(figsize=(8, 8))

    # Plotando gráfico e vetores
    plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)

    
    # Juntando todos os X e Y (início e fim) para o gráfico não cortar as pontas
    todos_x = X + [v[1][0] for v in vetores]
    todos_y = Y + [v[1][1] for v in vetores]
    plt.xlim(min(todos_x) - 1, max(todos_x) + 1)
    plt.ylim(min(todos_y) - 1, max(todos_y) + 1)

    # Desenhando os eixos centrais
    plt.axhline(0, color='black', linewidth=1.2)
    plt.axvline(0, color='black', linewidth=1.2)
    
    # Grade e textos
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title(titulo)

    plt.show()

"""
Criando vetores A e B com base na figura 1.2 da atividade:
    Basta passar os pontos X e Y de cada vetor para a função plotar_vetores
"""

lista_de_vetores_A = [
    ((0, 0), (1, 2)),
    ((1, 2), (5, -4)),
    ((0, 0), (5, -4)),
]

lista_de_vetores_B = [
    ((0, 0), (1, 2)),
    ((4, -6), (1, 2)),
    ((0, 0), (4, -6)),
]

"""
Plotando gráfico com vetores A e B
"""

plotar_vetores(lista_de_vetores_A, titulo="Gráfico de Vetores A")
plotar_vetores(lista_de_vetores_B, titulo="Gráfico de Vetores B")