# Solução de sistemas lineares pelo método da Fatoração LU
# A matriz é de ordem n x n e b é o vetor de termos independentes

import numpy as np

# ---------- ENTRADA ----------
A = np.array([[2.0, 1.0, 1.0],
              [4.0, -6.0, 0.0],
              [-2.0, 7.0, 2.0]])

b = np.array([5.0, -2.0, 9.0])

n = len(A)

# ---------- ETAPA 1: FATORAÇÃO LU ----------
L = np.zeros((n, n))
U = np.zeros((n, n))

for i in range(n):
    L[i, i] = 1.0  # diagonal de L igual a 1

for k in range(n):
    # Cálculo dos elementos da matriz U (linha k)
    for j in range(k, n):
        soma = 0.0
        for m in range(k):
            soma += L[k, m] * U[m, j]
        U[k, j] = A[k, j] - soma

    # Verificação de pivô nulo
    if abs(U[k, k]) < 1e-12:
        raise ValueError("Fatoração impossível: pivô nulo encontrado.")

    # Cálculo dos elementos da matriz L (coluna k)
    for i in range(k + 1, n):
        soma = 0.0
        for m in range(k):
            soma += L[i, m] * U[m, k]
        L[i, k] = (A[i, k] - soma) / U[k, k]

# ---------- ETAPA 2: SUBSTITUIÇÃO DIRETA (Ly = b) ----------
y = np.zeros(n)

for i in range(n):
    soma = 0.0
    for j in range(i):
        soma += L[i, j] * y[j]
    y[i] = b[i] - soma

# ---------- ETAPA 3: SUBSTITUIÇÃO RETROATIVA (Ux = y) ----------
x = np.zeros(n)

for i in range(n - 1, -1, -1):
    soma = 0.0
    for j in range(i + 1, n):
        soma += U[i, j] * x[j]
    x[i] = (y[i] - soma) / U[i, i]

# ---------- SAÍDA ----------
print("Matriz A:")
print(A)
print("\nMatriz L:")
print(L)
print("\nMatriz U:")
print(U)
print("\nVetor solução x:")
print(x)