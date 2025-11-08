import numpy as np

# -----------------------------------------------
# EXEMPLO: pontos para interpolação
# (x0, y0) = (0, 1)
# (x1, y1) = (1, 3)
# (x2, y2) = (2, 2)
# -----------------------------------------------
x = np.array([0.0, 1.0, 2.0])
y = np.array([1.0, 3.0, 2.0])

# -----------------------------------------------
# O grau do polinômio será n = número_de_pontos - 1
# Aqui temos 3 pontos, então grau = 2
# -----------------------------------------------
n = len(x) - 1

# -----------------------------------------------
# Montagem da matriz de Vandermonde
# V[i,j] = x[i]^j
# -----------------------------------------------
V = np.zeros((n+1, n+1))

for i in range(n+1):
    for j in range(n+1):
        V[i, j] = x[i] ** j

print("Matriz de Vandermonde:")
print(V)

# -----------------------------------------------
# Resolver o sistema V * a = y
# a = [a0, a1, ..., an]
# -----------------------------------------------
a = np.linalg.solve(V, y)

print("\nCoeficientes do polinômio:")
for i in range(n+1):
    print(f"a{i} = {a[i]}")

# -----------------------------------------------
# Montar o polinômio em forma simbólica (string)
# p(x) = a0 + a1 x + a2 x^2 + ...
# -----------------------------------------------
pol = "p(x) = "

for i in range(n+1):
    coef = a[i]
    
    # cria o termo
    if i == 0:
        termo = f"{coef:.4f}"
    elif i == 1:
        termo = f"{coef:.4f}·x"
    else:
        termo = f"{coef:.4f}·x^{i}"

    # adiciona com + entre os termos
    if i == 0:
        pol += termo
    else:
        pol += " + " + termo

print("\nPolinômio interpolador:")
print(pol)