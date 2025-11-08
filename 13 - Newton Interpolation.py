# ---------------------------------------------------------
# INTERPOLAÇÃO DE NEWTON DAS DIFERENÇAS DIVIDIDAS
# Simples, linear, sem def, sem poly1d, tudo na mão.
# ---------------------------------------------------------

# Pontos (x_i, y_i) do exemplo
x = [0.0, 1.0, 2.0]
y = [1.0, 3.0, 2.0]

n = len(x) - 1   # grau

# ---------------------------------------------------------
# 1) TABELA DE DIFERENÇAS DIVIDIDAS
# A tabela será armazenada como lista de listas:
# dd[i][j] = diferença dividida de ordem j começando em i
# ---------------------------------------------------------

dd = [[0.0]*(n+1) for _ in range(n+1)]

# Primeira coluna: valores de y
for i in range(n+1):
    dd[i][0] = y[i]

# Preenche as ordens seguintes
for j in range(1, n+1):            # ordem
    for i in range(n+1-j):         # linha
        dd[i][j] = (dd[i+1][j-1] - dd[i][j-1]) / (x[i+j] - x[i])

# Coeficientes do polinômio de Newton: a0, a1, ..., an
a = [dd[0][j] for j in range(n+1)]

# ---------------------------------------------------------
# 2) CONSTRUÇÃO DO POLINÔMIO EXPANDIDO
# P(x) = a0 + a1*(x-x0) + a2*(x-x0)(x-x1) + ...
#
# Representaremos polinômios como listas de coef:
# [c0, c1, c2, ...]  para c0 + c1*x + c2*x^2 + ...
# ---------------------------------------------------------

# Polinômio final
P = [0.0] * (n+1)

# Polinômio acumulador para os fatores (x - x0)(x - x1)...(x - x{k-1})
fator = [1.0]   # começa como 1

for k in range(n+1):

    # Soma a_k * fator ao polinômio P
    for i in range(len(fator)):
        P[i] += a[k] * fator[i]

    # Atualiza o fator (multiplica por x - x_k) para o próximo termo
    if k < n:
        novo = [0.0]*(len(fator)+1)
        for i in range(len(fator)):
            novo[i]     -= fator[i] * x[k]   # termo * (-x_k)
            novo[i+1]   += fator[i]          # termo * x
        fator = novo

# ---------------------------------------------------------
# 3) RESULTADOS
# ---------------------------------------------------------

print("Coeficientes de Newton (a_k):")
for i in range(n+1):
    print(f"a{i} = {a[i]}")

print("\nCoeficientes do polinômio expandido P(x) (ordem crescente):")
for i in range(len(P)):
    print(f"coef. de x^{i} = {P[i]}")

# Construir string legível
pol = ""
first = True
for i in range(len(P)-1, -1, -1):
    coef = P[i]
    if abs(coef) < 1e-14:
        continue
    if not first:
        pol += " + "
    first = False
    if i == 0:
        pol += f"{coef:.6g}"
    elif i == 1:
        pol += f"{coef:.6g}*x"
    else:
        pol += f"{coef:.6g}*x^{i}"

print("\nP(x) =")
print(pol)
