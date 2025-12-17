# ============================================================
# Interpolação de Lagrange (float padrão) -> polinômio EXPANDIDO
# 1) Expande P(x) = a0 + a1*x + ... + an*x^n
# 2) Imprime coeficientes e o polinômio
# 3) Cria a função P_eval(x) (Horner) e testa nos nós
#
# Obs.: com muitos pontos e x grandes, pode haver erro numérico ao avaliar
# o polinômio expandido em float. O código abaixo faz exatamente o pedido.
# ============================================================

# ---------- 1) Pontos ----------
# Esse conjunto é numericamente instável
#x_vals = [1872., 1890., 1900., 1920., 1940., 1950., 1960., 1970., 1980., 1991.] 
#y_vals = [9.9, 14.3, 17.4, 30.6, 41.2, 51.9, 70.2, 93.1, 119.0, 146.2]

x_vals = [1960., 1970., 1980., 1991]
y_vals = [70.2, 93.1, 119.0, 146.2]

N = len(x_vals)
if N != len(y_vals):
    raise ValueError("x_vals e y_vals devem ter o mesmo tamanho.")
if N < 2:
    raise ValueError("Forneça pelo menos 2 pontos.")

for i in range(N):
    for j in range(i + 1, N):
        if x_vals[i] == x_vals[j]:
            raise ValueError(f"Há x repetido: x[{i}] = x[{j}] = {x_vals[i]}")

n = N - 1  # grau

# ---------- 2) Expansão do polinômio por Lagrange ----------
# P[i] = coeficiente de x^i
P = [0.0] * (n + 1)

for k in range(N):
    numer = [1.0]   # Numer_k(x) = Π_{j≠k} (x - x_j), em coeficientes crescentes
    denom = 1.0     # Den_k = Π_{j≠k} (x_k - x_j)

    xk = x_vals[k]
    for j in range(N):
        if j == k:
            continue

        xj = x_vals[j]
        denom *= (xk - xj)

        # numer <- numer * (x - xj), onde (x - xj) = [-xj, 1]
        novo = [0.0] * (len(numer) + 1)
        for i, a in enumerate(numer):
            novo[i]     += a * (-xj)
            novo[i + 1] += a
        numer = novo

    escala = y_vals[k] / denom
    for i in range(n + 1):
        P[i] += escala * numer[i]

# ---------- 3) Imprimir coeficientes ----------
print(f"Grau do polinômio: n = {n}\n")

print("Coeficientes de P(x) (ordem crescente):")
for i, a in enumerate(P):
    print(f"  a_{i} (x^{i}) = {a:.16e}")

# ---------- 4) Imprimir polinômio expandido ----------
tol = 1e-14
texto = ""
primeiro = True

for p in range(n, -1, -1):
    a = P[p]
    if abs(a) < tol:
        continue

    sinal = "-" if a < 0 else "+"
    mag = f"{abs(a):.12g}"

    if p == 0:
        termo = f"{mag}"
    elif p == 1:
        termo = f"{mag}*x"
    else:
        termo = f"{mag}*x^{p}"

    if primeiro:
        texto += ("" if a >= 0 else "-") + termo
        primeiro = False
    else:
        texto += f" {sinal} {termo}"

print("\nP(x) expandido:")
print(texto if texto else "0")

# ---------- 5) Criar função para testar ----------
def P_eval(x):
    # Horner: avalia P[0] + P[1]x + ... + P[n]x^n
    r = 0.0
    for a in reversed(P):
        r = r * x + a
    return r

# Exemplo de uso:
print(P_eval(2000))
