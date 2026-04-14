import numpy as np

def transpor_manualmente(vetor_linha):

    n_elementos = vetor_linha.shape[1]

    # Criando molde com vetor nulo
    vetor_coluna = np.zeros((n_elementos, 1))
    
    for i in range(n_elementos):
        vetor_coluna[i][0] = vetor_linha[0][i]
        
    return vetor_coluna



"""
Testando a função transpor_manualmente
"""

vetor_linha = np.array([[3, -5, 7, 1]])
vetor_coluna = transpor_manualmente(vetor_linha)

print("Vetor linha (Original):")
print(vetor_linha, "\n")

print("Vetor coluna (Transposto):")
print(vetor_coluna)