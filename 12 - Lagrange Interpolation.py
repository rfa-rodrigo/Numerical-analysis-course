# ----------------------------------------------
# # Objetivo:
#   Dado (x_i, y_i), construir P(x) = sum_{k=0}^n y_k * L_k(x),
#   onde L_k(x) = prod_{j != k} (x - x_j)/(x_k - x_j)
#
# Passos:
#   1) Definir pontos (x_i, y_i)
#   2) Para cada k, construir o polinômio numerador de L_k(x) expandido:
#        Numer_k(x) = ∏_{j != k} (x - x_j)
#      - Fazemos isso multiplicando (convolução) listas de coeficientes.
#   3) Dividir Numer_k(x) pelo denominador Den_k = ∏_{j != k} (x_k - x_j)
#   4) Somar em P(x): P += y_k * (Numer_k/Den_k)
#   5) Exibir P(x) expandido e conferir P(x_i) ~ y_i
# ----------------------------------------------

# 1) Pontos (edite aqui, se desejar)
x_vals = [0.0, 1.0, 2.0]
y_vals = [1.0, 3.0, 2.0]

n = len(x_vals) - 1  # grau do polinômio

# 2) Vetor de coeficientes do polinômio P, no formato:
#    P[0] = termo constante, P[1] = coef. de x, ..., P[n] = coef. de x^n
P = [0.0] * (n + 1)

# 3) Loop pelos L_k
for k in range(n + 1):
    # Numerador de L_k(x): começa em 1 (polinômio constante)
    # Representado por lista de coeficientes [1.0]
    numer = [1.0]  # coeficientes em ordem crescente de potência
    denom = 1.0

    # Multiplicar todos os fatores (x - x_j), j != k
    for j in range(n + 1):
        if j == k:
            continue

        # Atualiza denom = ∏(x_k - x_j)
        denom *= (x_vals[k] - x_vals[j])

        # Convolução de 'numer' com o fator (x - x_j) = [ -x_j, 1 ] em ordem crescente:
        # (x - x_j) em coeficientes crescentes é [(-x_j), 1]  -> a0 + a1*x
        fator = [-x_vals[j], 1.0]
        novo = [0.0] * (len(numer) + 1)  # grau aumenta em 1 a cada multiplicação

        # Convolução manual (sem funções)
        for a_idx, a in enumerate(numer):
            # a * 1*x -> desloca em +1
            novo[a_idx + 1] += a * fator[1]
            # a * (-x_j) -> fica na mesma posição
            novo[a_idx] += a * fator[0]

        numer = novo  # atualiza o numerador expandido

    # Agora L_k(x) = numer / denom
    # Escalar numer por y_k/denom e somar em P
    escala = y_vals[k] / denom
    for t in range(len(numer)):
        P[t] += escala * numer[t]

# 4) Exibir resultados
print("Pontos (x_i, y_i):")
for xi, yi in zip(x_vals, y_vals):
    print(f"  ({xi:.6g}, {yi:.6g})")

print(f"\nGrau do polinômio: n = {n}")

# Coeficientes de P(x) (ordem crescente: constante, x, x^2, ...)
print("\nCoeficientes de P(x) (ordem crescente):")
for idx, c in enumerate(P):
    print(f"  a_{idx} (x^{idx}) = {c:.12g}")

# Forma legível P(x) = a_n x^n + ... + a_1 x + a_0
termos = []
deg = len(P) - 1
for p in range(deg, -1, -1):
    a = P[p]
    if abs(a) < 1e-14:
        continue
    if p == 0:
        termos.append(f"{a:.12g}")
    elif p == 1:
        termos.append(f"{a:.12g}*x")
    else:
        termos.append(f"{a:.12g}*x^{p}")

print("\nPolinômio interpolador P(x) expandido:")
print(" + ".join(termos) if termos else "0")