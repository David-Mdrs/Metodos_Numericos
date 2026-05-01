import numpy as np

# Definindo os vetores e os pesos (escalares)
vetor_1 = np.array([3, 0, 6])
vetor_2 = np.array([1, 2, 5])
pesos = np.array([4, 3])

# Criando a matriz_A com as colunas sendo os vetores
matriz_A = np.column_stack((vetor_1, vetor_2))

# Calculando o resultado da multiplicação matriz-vetor
resultado_matriz = matriz_A @ pesos

# Comparando com o método manual para confirmar
resultado_manual = pesos[0] * vetor_1 + pesos[1] * vetor_2

diferenca = np.abs(resultado_matriz - resultado_manual)

limite_erro = 1e-15
sao_iguais = np.max(diferenca) < limite_erro

print("Resultado da matriz vetor:  ", resultado_matriz)
print("Resultado manual:           ", resultado_manual)
print("\nResultados são iguais:      ", sao_iguais)
print("Maior diferença encontrada: ", np.max(diferenca))