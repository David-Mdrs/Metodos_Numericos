import numpy as np

# Criando vetores aleatórios
t = np.random.randint(-5, 6, 2)
r = np.random.randint(-5, 6, 2)

if np.all(r == 0): r = np.array([2, 1])
if np.all(t == 0): t = np.array([1, 2])

# Colocando bug de propósito (beta bugado)
beta_bug = np.dot(t, r) / np.dot(t, t) 

# Calculando as componentes com o beta bugado
t_paralelo_bug = beta_bug * r
t_perpendicular_bug = t - t_paralelo_bug

print("Verificação de Sanidade\n")

# Teste 01: t_paralelo + t_perpendicular == t
soma = t_paralelo_bug + t_perpendicular_bug
passou_soma = np.allclose(soma, t)

if not passou_soma:
    print(f"Teste 01 (Soma): ERRO. Soma resultou em {soma} (deveria ser {t})")
else:
    print("Teste 01 (Soma): PASSOU")

# Teste 02: Produto escalar == 0 (Ortogonalidade)
produto_escalar = np.dot(t_paralelo_bug, t_perpendicular_bug)
passou_ortogonalidade = np.isclose(produto_escalar, 0)

if not passou_ortogonalidade:
    print(f"Teste 02 (Ortogonalidade): ERRO. Produto escalar resultou em {produto_escalar} (deveria ser 0)")
else:
    print("Teste 02 (Ortogonalidade): PASSOU")