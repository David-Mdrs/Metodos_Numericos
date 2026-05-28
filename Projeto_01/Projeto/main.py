"""
Agora que temos o código base para restauração de uma única imagem, podemos fazer um código que:
    - Testa as 10 imagens da pasta "imagens_originais";
    - Salva os resultados na pasta "imagens_restauradas".
"""

import os
import cv2
import numpy as np
import scipy.linalg as sla

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_ORIGINAIS = os.path.join(BASE_DIR, "imagens_originais")
PASTA_RESTAURADAS = os.path.join(BASE_DIR, "imagens_restauradas")


# Criando pasta de saída se não existir
os.makedirs(PASTA_RESTAURADAS, exist_ok=True)


# Pegando as 10 imagens da pasta de entrada
arquivos = os.listdir(PASTA_ORIGINAIS)[:10]


# Início do processamento de cada imagem
for nome_arquivo in arquivos:

    # Carregando imagens
    caminho = os.path.join(PASTA_ORIGINAIS, nome_arquivo)
    imagem = cv2.imread(caminho)
    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)


    # Criando máscara de pixels corrompidos
    imagem_corrompida = imagem_rgb.copy()

    linha_inicio = 100
    linha_fim = 120

    coluna_inicio = 100
    coluna_fim = 110

    imagem_corrompida[
        linha_inicio:linha_fim,
        coluna_inicio:coluna_fim
    ] = [255,255,255]


    # Mapeando pixels corrompidos
    indices = {}
    contador = 0

    for i in range(linha_inicio, linha_fim):
        for j in range(coluna_inicio, coluna_fim):
            indices[(i,j)] = contador
            contador += 1

    n = contador


    # Montando matriz A e vetores b
    A = np.zeros((n,n))

    b_r = np.zeros(n)
    b_g = np.zeros(n)
    b_b = np.zeros(n)

    for (i,j), k in indices.items():
        A[k,k] = -4

        vizinhos = [
            (i-1,j),
            (i+1,j),
            (i,j-1),
            (i,j+1)
        ]

        for vi,vj in vizinhos:
            if (vi,vj) in indices:
                indice_vizinho = indices[(vi,vj)]
                A[k,indice_vizinho] = 1
            else:
                b_r[k] -= imagem_rgb[vi,vj,0]
                b_g[k] -= imagem_rgb[vi,vj,1]
                b_b[k] -= imagem_rgb[vi,vj,2]


    # Resolvendo sistema LU
    LU, piv = sla.lu_factor(A)

    x_r = sla.lu_solve((LU,piv), b_r)
    x_g = sla.lu_solve((LU,piv), b_g)
    x_b = sla.lu_solve((LU,piv), b_b)

    # Reconstruindo imagem
    imagem_reconstruida = imagem_corrompida.copy()

    for (i,j), k in indices.items():
        r = int(np.clip(x_r[k],0,255))
        g = int(np.clip(x_g[k],0,255))
        b = int(np.clip(x_b[k],0,255))

        imagem_reconstruida[i,j] = [r,g,b]


    # Salvando imagem reconstruída
    imagem_bgr = cv2.cvtColor(
        imagem_reconstruida,
        cv2.COLOR_RGB2BGR
    )

    cv2.imwrite(
        os.path.join(PASTA_RESTAURADAS, nome_arquivo),
        imagem_bgr
    )