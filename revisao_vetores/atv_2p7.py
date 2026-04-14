import numpy as np

def produto_escalar(a, b):
    soma = 0

    for i in range(len(a)):
        soma += a[i] * b[i]
    return soma

# Vetores aleatórios para exemplo
vetor_a = np.array([2, 4, -1, 0, 3])
vetor_b = np.array([5, 1, 9, -2, 6])

# Calculando o produto escalar em ordem A x B e B x A
produto_ab = produto_escalar(vetor_a, vetor_b)
produto_ba = produto_escalar(vetor_b, vetor_a)

print("Vetor A: ", vetor_a)
print("Vetor B: ", vetor_b, "\n")

print(f"Produto Escalar (A x B): {produto_ab:.6f}")
print(f"Produto Escalar (B x A): {produto_ba:.6f}\n")


# Teste final
if produto_ab == produto_ba:
    print("COMPROVADO: O produto escalar é comutativo!")
else:
    print("ERRO: Os resultados deram diferentes.")