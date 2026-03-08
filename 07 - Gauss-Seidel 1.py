# Sistema de equações:
#  4x1 -  x2 + 0x3 = 15
# -x1 + 4x2 -  x3 = 10
#  0x1 -  x2 + 3x3 = 10
#
# Solução exata esperada: x1 = 5, x2 = 5, x3 = 5

# ----------------------------
# Gauss-Seidel
# ----------------------------

A = [
    [ 4.0, -1.0,  0.0],
    [-1.0,  4.0, -1.0],
    [ 0.0, -1.0,  3.0],
]
b = [15.0, 10.0, 10.0]

n   = len(A)
TOL = 1e-8       # tolerância
N   = 1000       # máximo de iterações
X0  = [0.0]*n    # chute inicial x^(0)

# --- Step 1 ---
k = 1

# --- Step 2 ---
while k <= N:
    # guardamos cópia para testar ||x - X0||_inf (x será o novo vetor)
    x = X0[:]  # começamos da estimativa anterior

    # --- Step 3: atualização Gauss-Seidel (usa valores "mais novos" assim que computados) ---
    for i in range(n):
        soma = 0.0
        # parte com j < i usa x[j] já atualizado
        for j in range(0, i):
            soma += A[i][j]*x[j]
        # parte com j > i usa X0[j] da iteração anterior
        for j in range(i+1, n):
            soma += A[i][j]*X0[j]
        x[i] = ( -soma + b[i] ) / A[i][i]

    # --- Step 4: teste de parada com norma infinito ---
    diff_inf = max(abs(x[i] - X0[i]) for i in range(n))
    if diff_inf < TOL:
        print("Solução aproximada (convergência alcançada):")
        print(x)
        print(f"Iterações: {k}, ||x - X0||_inf = {diff_inf:.3e}")
        break

    # --- Step 5 ---
    k = k + 1

    # --- Step 6: preparar próxima iteração: X0 ← x ---
    X0 = x[:]
else:
    # --- Step 7 ---
    print("Maximum number of iterations exceeded")
    print("Última aproximação:", X0)