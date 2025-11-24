# Integração numérica – Regra de Newton–Cotes fechada (ordem n)
# n = número de subintervalos → n+1 pontos igualmente espaçados

import numpy as np
import math

# ------------------------------------------
# 1. DEFINIÇÃO DA FUNÇÃO, INTERVALO E ORDEM
# ------------------------------------------
# Edite aqui:
f = lambda x: math.sin(x)  # função a ser integrada
a = 0.0                    # limite inferior
b = math.pi                # limite superior
n = 2                      # ordem de Newton–Cotes (1=trapézio, 2=Simpson, etc.)

# Atenção: na prática, n não deve ser muito grande (tipicamente n ≤ 6)
if n < 1:
    raise ValueError("Use n >= 1 para Newton–Cotes fechado.")

# ------------------------------------------
# 2. NÓS EM [0,1] E MATRIZ DE MOMENTOS
#    t_i = i/n, i=0,...,n  (n+1 pontos)
# ------------------------------------------
t = np.linspace(0.0, 1.0, n + 1)  # nós em [0,1]

# Matriz de potências: A[i,k] = t_i^k
# Para k = 0,...,n  (momentos até grau n)
A = np.zeros((n + 1, n + 1))
for i in range(n + 1):
    for k in range(n + 1):
        A[i, k] = t[i]**k

# Vetor de momentos exatos de 1 em [0,1]: b_k = ∫_0^1 t^k dt = 1/(k+1)
b_mom = np.zeros(n + 1)
for k in range(n + 1):
    b_mom[k] = 1.0 / (k + 1)

# ------------------------------------------
# 3. CÁLCULO DOS PESOS w_i
#    Precisamos que ∑_i w_i t_i^k = 1/(k+1), k=0,...,n
#    Em forma matricial: (A^T) * w = b_mom
# ------------------------------------------
w = np.linalg.solve(A.T, b_mom)

# ------------------------------------------
# 4. APLICAÇÃO DA FÓRMULA EM [a,b]
#    x_i = a + (b-a)*t_i
#    ∫_a^b f(x) dx ≈ (b-a) * ∑_i w_i f(x_i)
# ------------------------------------------
integral_aprox = 0.0
for i in range(n + 1):
    x_i = a + (b - a) * t[i]
    integral_aprox += w[i] * f(x_i)

integral_aprox *= (b - a)

# ------------------------------------------
# 5. SAÍDA
# ------------------------------------------
print("Regra de Newton–Cotes fechada")
print(f"Ordem n = {n} (n subintervalos, {n+1} pontos)")
print(f"Intervalo [{a}, {b}]")
print("\nPesos w_i em [0,1]:")
for i in range(n + 1):
    print(f"w_{i} = {w[i]}")

print(f"\nIntegral aproximada = {integral_aprox:.10f}")