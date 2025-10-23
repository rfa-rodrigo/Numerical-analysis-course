# Solução de sistemas lineares Ax = b pelo método de Cholesky
# A é simétrica e definida positiva: A = L * L^T

import numpy as np

# ---------- ENTRADA ----------
A = np.array([[4.0, 2.0, -2.0],
              [2.0, 2.0, -1.0],
              [-2.0, -1.0, 5.0]])

b = np.array([6.0, 3.0, 5.0])

n = len(A)

# ---------- ETAPA 1: FATORAÇÃO DE CHOLESKY ----------
L = np.zeros((n, n))

for i in range(n):
    # Cálculo de L[i,i]
    soma = 0.0
    for k in range(i):
        soma += L[i, k]**2
    L[i, i] = np.sqrt(A[i, i] - soma)

    # Cálculo dos elementos abaixo da diagonal
    for j in range(i + 1, n):
        soma = 0.0
        for k in range(i):
            soma += L[j, k] * L[i, k]
        L[j, i] = (A[j, i] - soma) / L[i, i]

# ---------- ETAPA 2: SUBSTITUIÇÃO DIRETA (L * y = b) ----------
y = np.zeros(n)

for i in range(n):
    soma = 0.0
    for j in range(i):
        soma += L[i, j] * y[j]
    y[i] = (b[i] - soma) / L[i, i]

# ---------- ETAPA 3: SUBSTITUIÇÃO RETROATIVA (L^T * x = y) ----------
x = np.zeros(n)

for i in range(n - 1, -1, -1):
    soma = 0.0
    for j in range(i + 1, n):
        soma += L[j, i] * x[j]
    x[i] = (y[i] - soma) / L[i, i]

# ---------- SAÍDA ----------
print("Matriz A:")
print(A)
print("\nMatriz L (triangular inferior):")
print(L)
print("\nMatriz L^T (transposta):")
print(L.T)
print("\nVetor solução x:")
print(x)