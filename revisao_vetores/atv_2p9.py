import matplotlib.pyplot as plt
import numpy as np

"""
Utilizando a mesma função da questão 02.2
"""

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

import numpy as np

#  Vetores aleatórios T e R
t = np.random.randint(-5, 6, 2)
r = np.random.randint(-5, 6, 2)

# Evitando o zero absoluto no r (divisão por 0)
if np.all(r == 0): r = np.array([2, 1]) 

# Componente paralela
beta = np.dot(t, r) / np.dot(r, r)
t_paralelo = beta * r

# Componente perpendicular
t_perpendicular = t - t_paralelo



# Passando coordenadas dos vetores para a função plotar_vetores
lista_decomposicao = [
    ((0, 0), (r[0], r[1])),
    ((0, 0), (t[0], t[1])),
    ((0, 0), (t_perpendicular[0], t_perpendicular[1]))
]

plotar_vetores(lista_decomposicao, titulo="Decomposição Ortogonal (t || r e t ⊥ r)")