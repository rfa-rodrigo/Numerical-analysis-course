import numpy as np

# ============================================
# 1) DEFINIÇÃO DAS FUNÇÕES g_j E DOS DADOS
# ============================================

# Exemplo: o usuário escolhe as funções
# g1(x) = 1
# g2(x) = x
# g3(x) = sin(x)
g_list = [
    #lambda x: 1.0,
    lambda x: x**2,
    #lambda x: np.sin(x)
]

# número de funções (n)
n = len(g_list)

# Pontos experimentais (x_k, f(x_k))
x_data = np.array([-1.0, -0.75, -0.6, -0.5, -0.3, 0.0, 0.2, 0.4, 0.5, 0.7, 1.0])
y_data = np.array([2.05, 1.153, 0.45, 0.4, 0.5, 0.0, 0.2, 0.6, 0.512, 1.2, 2.05])

m = len(x_data)   # número de pontos

# =================================================
# 2) MONTAGEM DA MATRIZ G COM g_j(x_k)
#    G_{k,j} = g_j(x_k)
# =================================================
G = np.zeros((m, n))

for k in range(m):
    xk = x_data[k]
    for j in range(n):
        G[k, j] = g_list[j](xk)

# =================================================
# 3) MONTAGEM DAS EQUAÇÕES NORMAIS A α = b
#    A_ij = Σ_k g_i(x_k) g_j(x_k)
#    b_i  = Σ_k f(x_k) g_i(x_k)
# =================================================
A = np.zeros((n, n))
b = np.zeros(n)

# matriz A
for i in range(n):
    for j in range(n):
        soma = 0.0
        for k in range(m):
            soma += G[k, i] * G[k, j]
        A[i, j] = soma

# vetor b
for i in range(n):
    soma = 0.0
    for k in range(m):
        soma += y_data[k] * G[k, i]
    b[i] = soma

# =================================================
# 4) RESOLUÇÃO DO SISTEMA LINEAR
# =================================================
alpha = np.linalg.solve(A, b)

print("Coeficientes do ajuste (α_j):")
for j in range(n):
    print(f"alpha_{j+1} = {alpha[j]}")

# =================================================
# 5) USO DO MODELO AJUSTADO
#    φ(x) = Σ_j α_j g_j(x)
#    (exemplo: calcular φ nos pontos originais)
# =================================================
print("\nComparação nos pontos de dados:")
for k in range(m):
    xk = x_data[k]
    fx = y_data[k]
    phi_x = 0.0
    for j in range(n):
        phi_x += alpha[j] * g_list[j](xk)
    print(f"x = {xk:5.2f} | f(x) = {fx:7.4f} | φ(x) = {phi_x:7.4f}")