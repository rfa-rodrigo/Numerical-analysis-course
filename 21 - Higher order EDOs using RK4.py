# ==============================================
# Runge-Kutta clássico de 4ª ordem para SISTEMAS
# Segue o algoritmo da figura (Burden & Faires)
# u_j' = f_j(t, u1, ..., um), j = 1,...,m
# ==============================================

# -------------------------------
# CONFIGURAÇÃO DO PROBLEMA
# -------------------------------

# Número de equações do sistema (m)
m = 2

# Definição das funções f_j(t, u1, ..., um) via lambda
# Exemplo: sistema equivalente à EDO de 2ª ordem y'' = -2y' - 5y
# u1 = y, u2 = y'
f = []
f.append(lambda t, u1, u2: u2)              # u1' = u2
f.append(lambda t, u1, u2: -2.0*u2 - 5.0*u1) # u2' = -2u2 - 5u1

# Intervalo [a, b]
a = 0.0
b = 1.0

# Número de subintervalos
N = 10

# Condições iniciais: alpha_j = u_j(a), j = 1,...,m
alpha = [1.0, 0.0]   # para o exemplo acima: y(0)=1, y'(0)=0

# ------------------------------------------------
# ALGORITMO DE RUNGE-KUTTA 4ª ORDEM (SISTEMA)
# ------------------------------------------------

h = (b - a) / N     # Step 1: h
t = a               # Step 1: t = a

# Step 2: w_j = alpha_j
w = alpha[:]        # cópia

# Step 3: saída inicial
print("t", " ".join([f"u{j+1}" for j in range(m)]))
print(f"{t:.6f}", " ".join([f"{w[j]:.6f}" for j in range(m)]))

# Step 4: laço principal i = 1,...,N
for i in range(1, N+1):

    # Step 5: k1_j = h f_j(t, w1,...,wm)
    k1 = [0.0]*m
    for j in range(m):
        k1[j] = h * f[j](t, *w)

    # Step 6: k2_j = h f_j(t + h/2, w1+1/2 k11, ..., wm+1/2 k1m)
    u_temp = [0.0]*m
    for j in range(m):
        u_temp[j] = w[j] + 0.5*k1[j]
    k2 = [0.0]*m
    for j in range(m):
        k2[j] = h * f[j](t + 0.5*h, *u_temp)

    # Step 7: k3_j = h f_j(t + h/2, w1+1/2 k21, ..., wm+1/2 k2m)
    for j in range(m):
        u_temp[j] = w[j] + 0.5*k2[j]
    k3 = [0.0]*m
    for j in range(m):
        k3[j] = h * f[j](t + 0.5*h, *u_temp)

    # Step 8: k4_j = h f_j(t + h, w1+k31, ..., wm+k3m)
    for j in range(m):
        u_temp[j] = w[j] + k3[j]
    k4 = [0.0]*m
    for j in range(m):
        k4[j] = h * f[j](t + h, *u_temp)

    # Step 9: w_j = w_j + (k1_j + 2k2_j + 2k3_j + k4_j)/6
    for j in range(m):
        w[j] = w[j] + (k1[j] + 2.0*k2[j] + 2.0*k3[j] + k4[j]) / 6.0

    # Step 10: t = a + i*h
    t = a + i*h

    # Step 11: OUTPUT(t, w1,...,wm)
    print(f"{t:.6f}", " ".join([f"{w[j]:.6f}" for j in range(m)]))

# Step 12: STOP (fim do script)