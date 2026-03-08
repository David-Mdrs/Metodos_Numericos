import numpy as np

a = float(input("Digite um número positivo para extrair a raiz: "))

valor_real = np.sqrt(a)
xi = 1.0 
tentativas = 10

print("Interação | Aproximação (xi) | Erro Relativo")
for i in range(1, 11):
    xi = (xi + a / xi) / 2
    
    erro_relativo = abs(valor_real - xi) / valor_real

    print("Interação:        ", i)
    print("Aproximação (xi): ", xi)
    print("Erro Relativo:    ", erro_relativo, "\n")

    if (erro_relativo == 0):
        tentativas = i
        break

print(f"Convergência alcançada!\n")

print(f"Resultado final após {tentativas} voltas: {xi}")
print(f"Valor real no sistema:         {valor_real}")