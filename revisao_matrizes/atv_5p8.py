import numpy as np

def verificar_simetria(matriz):
    # Só existe matriz simétrica se for quadrada
    if matriz.shape[0] != matriz.shape[1]:
        return False
    
    diferenca = np.abs(matriz - matriz.T)
    tolerancia = 1e-15

    simetria = np.max(diferenca) < tolerancia
    
    return simetria


matriz_simetrica = np.array([[1, 2, 3],
                             [2, 4, 5],
                             [3, 5, 6]])

matriz_nao_simetrica = np.random.randn(3, 3)

matriz_retangular = np.array([[1, 2], [2, 1], [3, 3]])



print(f"Matriz 1 (simétrica):  {verificar_simetria(matriz_simetrica)}")
print(f"Matriz 2 (aleatória):  {verificar_simetria(matriz_nao_simetrica)}")
print(f"Matriz 3 (retangular): {verificar_simetria(matriz_retangular)}")
