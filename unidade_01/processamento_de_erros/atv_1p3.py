import numpy as np

x = 1/3

print("n | Valor de x(n)")
print("-" * 35)

for n in range(1, 10):
    print(f"{n} | {x}")
    x = (4 * x) - 1