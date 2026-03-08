# Sistema de equações:
#  4x1 -  x2 + 0x3 = 15
# -x1 + 4x2 -  x3 = 10
#  0x1 -  x2 + 3x3 = 10
#
# Solução exata esperada: x1 = 5, x2 = 5, x3 = 5

# ---------------------------
# Gauss-Jacobi 
# ---------------------------

A = [
    [ 4.0, -1.0,  0.0],
    [-1.0,  4.0, -1.0],
    [ 0.0, -1.0,  3.0],
]
b = [15.0, 10.0, 10.0]

n = len(A)
# Parâmetros do algoritmo
TOL = 1e-8          # tolerância
N   = 1000          # número máximo de iterações
X0  = [0.0]*n       # chute inicial x^(0)

# --- Step 1 ---
k = 1

# --- Step 2 ---
while k <= N:
    # --- Step 3: computar x^(k) a partir de X0 (Jacobi usa somente valores da iteração anterior) ---
    x = [0.0]*n
    for i in range(n):
        soma = 0.0
        for j in range(n):
            if j != i:
                soma += A[i][j]*X0[j]
        x[i] = ( -soma + b[i] ) / A[i][i]

    # --- Step 4: teste de parada  ||x - X0||_inf < TOL ---
    diff_inf = max(abs(x[i] - X0[i]) for i in range(n))
    if diff_inf < TOL:
        print("Solução aproximada (convergência alcançada):")
        print(x)
        print(f"Iterações: {k}, ||x - X0||_inf = {diff_inf:.3e}")
        break

    # --- Step 5 ---
    k = k + 1

    # --- Step 6: preparar próxima iteração: X0 ← x ---
    for i in range(n):
        X0[i] = x[i]
else:
    # --- Step 7 ---
    print("Maximum number of iterations exceeded")
    print("Última aproximação:", X0)
