import numpy as np

def norma_vetor(vetor):
    """
    Deve-se passar uma lista de componentes do vetor, no seguinte formato:
        [v1, v2, v3, ..., vn]
    """

    somatorio = 0
    for componente in vetor:
        somatorio += componente ** 2
    return np.sqrt(somatorio)


"""
Comparando função norma_vetor com a função np.linalg.norm
"""

vetor = np.array([3, -5, 7, 1])

print("Norma do vetor usando a função norma_vetor:   ", norma_vetor(vetor))
print("Norma do vetor usando a função np.linalg.norm:", np.linalg.norm(vetor))