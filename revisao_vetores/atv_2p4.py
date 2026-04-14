import numpy as np

def redimensionar_vetor(vetor, escalar):
    
    tamanho_atual = np.linalg.norm(vetor)
    
    # Proteção contra o vetor de zeros
    if tamanho_atual == 0:
        print("Erro: Vetor de zeros não possui direção. Impossível normalizar.")
        return vetor
        
    # Normalização do vetor
    vetor_unitario = vetor / tamanho_atual

    # Redimensionamento do vetor unitário
    vetor_redimensionado = vetor_unitario * escalar

    return vetor_redimensionado


"""
Testando a função redimensionar_vetor
"""

vetor = np.array([3, -5, 7, 1])
vetor_nulo = np.array([0, 0, 0, 0])

print("Calculando o vetor redimensionado normal:")
print(redimensionar_vetor(vetor, 5), "\n")

print("Calculando o vetor redimensionado de um vetor nulo:")
print(redimensionar_vetor(vetor_nulo, 5))