from time import perf_counter
import random

# Sistema de teste: tridiagonal SPD (Poisson 1D)
def build_system(n):
    A = [[0.0]*n for _ in range(n)]
    for i in range(n):
        A[i][i] = 2.0
        if i > 0:     A[i][i-1] = -1.0
        if i < n-1:   A[i][i+1] = -1.0
    b = [1.0]*n
    return A, b

def build_system_neutro(n, seed=42):
    random.seed(seed)
    A = [[random.uniform(-1, 1) for _ in range(n)] for _ in range(n)]
    b = [random.uniform(-5, 5) for _ in range(n)]
    
    # reforçar diagonal para garantir dominância
    for i in range(n):
        soma = sum(abs(A[i][j]) for j in range(n) if j != i)
        A[i][i] = soma + random.uniform(1.0, 2.0)  # diagonal > soma das outras
    
    return A, b

# ----------------- Métodos -----------------

def gauss_elim(A, b):
    n = len(A)
    aug = [A[i][:] + [b[i]] for i in range(n)]
    t0 = perf_counter()
    # eliminação
    for i in range(n-1):
        if abs(aug[i][i]) < 1e-14: return None, None, None
        for j in range(i+1, n):
            m = aug[j][i] / aug[i][i]
            for k in range(i, n+1):
                aug[j][k] -= m * aug[i][k]
    if abs(aug[n-1][n-1]) < 1e-14: return None, None, None
    # retro
    x = [0.0]*n
    x[n-1] = aug[n-1][n] / aug[n-1][n-1]
    for i in range(n-2, -1, -1):
        s = sum(aug[i][j]*x[j] for j in range(i+1, n))
        x[i] = (aug[i][n] - s) / aug[i][i]
    t1 = perf_counter()
    return x, (t1-t0), None  # sem iterações

def jacobi(A, b, tol=1e-8, Nmax=200000):
    n = len(A)
    X0 = [0.0]*n
    t0 = perf_counter()
    for k in range(1, Nmax+1):
        x = [0.0]*n
        for i in range(n):
            s = sum(A[i][j]*X0[j] for j in range(n) if j != i)
            x[i] = (b[i] - s)/A[i][i]
        diff = max(abs(x[i]-X0[i]) for i in range(n))
        if diff < tol:
            t1 = perf_counter()
            return x, (t1-t0), k
        X0 = x
    t1 = perf_counter()
    return X0, (t1-t0), Nmax

def seidel(A, b, tol=1e-8, Nmax=200000):
    n = len(A)
    X0 = [0.0]*n
    t0 = perf_counter()
    for k in range(1, Nmax+1):
        x = X0[:]
        for i in range(n):
            s1 = sum(A[i][j]*x[j] for j in range(i))
            s2 = sum(A[i][j]*X0[j] for j in range(i+1,n))
            x[i] = (b[i] - (s1+s2))/A[i][i]
        diff = max(abs(x[i]-X0[i]) for i in range(n))
        if diff < tol:
            t1 = perf_counter()
            return x, (t1-t0), k
        X0 = x
    t1 = perf_counter()
    return X0, (t1-t0), Nmax

# ----------------- Comparação -----------------


#A, b = build_system(n)
A, b = build_system_neutro(n, seed=42)

x_ge, t_ge, _ = gauss_elim(A, b)
print("Gauss-eliminação:")
print(f"tempo: {t_ge:.3f} s")

x_j, t_j, it_j = jacobi(A, b)
print("\nJacobi:")
print(f"tempo: {t_j:.3f} s | iterações: {it_j}")

x_s, t_s, it_s = seidel(A, b)
print("\nSeidel:")
print(f"tempo: {t_s:.3f} s | iterações: {it_s}")