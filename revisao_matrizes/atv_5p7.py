import numpy as np

# 1) Criando as matrizes aleatórias conforme os tamanhos do exercício
matriz_L = np.random.randn(2, 6) # L
matriz_I = np.random.randn(6, 3) # I
matriz_V = np.random.randn(3, 5) # V
matriz_E = np.random.randn(5, 2) # E

# 2) Multiplicando tudo e transpondo o resultado final
resultado_passo_2 = (matriz_L @ matriz_I @ matriz_V @ matriz_E).T

# 3) Transpondo individualmente e multiplicando na ordem original
try:
    resultado_passo_3 = matriz_L.T @ matriz_I.T @ matriz_V.T @ matriz_E.T
except ValueError as erro:
    resultado_passo_3 = f"Erro de Dimensão: {erro}"

# 4) Transpondo individualmente e multiplicando na ordem reversa
resultado_passo_4 = matriz_E.T @ matriz_V.T @ matriz_I.T @ matriz_L.T

# Verificações
print("\nTestando matrizes retangulares")
print(f"Passo 3: {resultado_passo_3}")
print(f"Passo 2 é igual ao Passo 4? {np.allclose(resultado_passo_2, resultado_passo_4)}")

# 5) Repetindo o processo com matrizes quadradas
tamanho = 4
matriz_L_quad = np.random.randn(tamanho, tamanho)
matriz_I_quad = np.random.randn(tamanho, tamanho)
matriz_V_quad = np.random.randn(tamanho, tamanho)
matriz_E_quad = np.random.randn(tamanho, tamanho)

resultado_quad_2 = (matriz_L_quad @ matriz_I_quad @ matriz_V_quad @ matriz_E_quad).T
resultado_quad_3 = matriz_L_quad.T @ matriz_I_quad.T @ matriz_V_quad.T @ matriz_E_quad.T
resultado_quad_4 = matriz_E_quad.T @ matriz_V_quad.T @ matriz_I_quad.T @ matriz_L_quad.T

print("\nTestando matrizes quadradas")
print(f"Passo 2 igual ao 3? {np.allclose(resultado_quad_2, resultado_quad_3)}")
print(f"Passo 2 igual ao 4? {np.allclose(resultado_quad_2, resultado_quad_4)}")