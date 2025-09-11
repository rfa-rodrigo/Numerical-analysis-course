# Sistema:
#  2x +  y -  z =  8
# -3x - y + 2z = -11
# -2x + y + 2z = -3

# Matriz aumentada [A|b]
A = [
    [ 2.0,  1.0, -1.0,  8.0],
    [-3.0, -1.0,  2.0, -11.0],
    [-2.0,  1.0,  2.0, -3.0],
]

n = len(A)
tol = 1e-12

# ---------- Elimination process ----------
for i in range(n - 1):
    # Step 2: encontrar pivô
    p = None
    for r in range(i, n):
        if abs(A[r][i]) > tol:
            p = r
            break
    if p is None:
        raise ValueError("no unique solution exists")

    # Step 3: troca de linhas, se necessário
    if p != i:
        A[i], A[p] = A[p], A[i]

    # Step 4-6: eliminação
    aii = A[i][i]
    for j in range(i + 1, n):
        mji = A[j][i] / aii
        for k in range(i, n + 1):
            A[j][k] -= mji * A[i][k]

# Step 7: verificar pivô final
if abs(A[n - 1][n - 1]) <= tol:
    raise ValueError("no unique solution exists")

# ---------- Backward substitution ----------
x = [0.0] * n
x[n - 1] = A[n - 1][n] / A[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    s = 0.0
    for j in range(i + 1, n):
        s += A[i][j] * x[j]
    x[i] = (A[i][n] - s) / A[i][i]

print("Solução:", x)
