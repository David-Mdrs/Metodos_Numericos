import numpy as np

linhas, colunas = 3, 4
matriz_A = np.random.randn(linhas, colunas)
matriz_B = np.random.randn(linhas, colunas)
escalar = np.random.randn()

# Testes da questão
resposta_1 = escalar * (matriz_A + matriz_B)
resposta_2 = escalar*matriz_A + escalar*matriz_B
resposta_3 = matriz_A*escalar + matriz_B*escalar

# Analisando igualdades
teste_1_2 = np.allclose(resposta_1, resposta_2)
teste_2_3 = np.allclose(resposta_2, resposta_3)

print(f"Escalar (sigma):       {escalar:.4f}\n")
print(f"Expressão 1 igual a 2? {teste_1_2}")
print(f"Expressão 2 igual a 3? {teste_2_3}")

if teste_1_2 and teste_2_3:
    print("\nAmbas as propriedades funcionaram!")