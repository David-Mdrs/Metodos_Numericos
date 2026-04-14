import numpy as np

def vetor_unitario(vetor):
    
    tamanho_real = np.linalg.norm(vetor)
    
    # Proteção contra o vetor nulo
    if tamanho_real == 0:
        print("Erro: Vetor de zeros não possui direção. Impossível normalizar.")
        return vetor
        
    # Normalização do vetor
    vetor_unitario = (1 / tamanho_real) * vetor
    
    return vetor_unitario


"""
Testando a função vetor_unitario
"""

vetor = np.array([3, -5, 7, 1])
vetor_nulo = np.array([0, 0, 0, 0])

print("Calculando o vetor unitário de um vetor normal:\n", vetor_unitario(vetor), "\n")
print("Calculando o vetor unitário de um vetor nulo:\n", vetor_unitario(vetor_nulo))