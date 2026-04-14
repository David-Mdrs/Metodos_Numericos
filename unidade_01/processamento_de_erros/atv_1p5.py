import numpy as nd

def funcao(x):
    return ((1 + x) - 1) / x

print("x      | Valor de f(x)")

print(10**(-12), " | ", funcao(10**(-12)))
print(10**(-15), " | " ,funcao(10**(-15)))
print(10**(-17), " | ", funcao(10**(-17)))

"""
A função é perigosa porque ocorre perda de significância. 
Ao somar 1 com um x muito pequeno, o computador arredonda o 
resultado para 1, fazendo o numerador virar zero.
"""