# Método de Runge-Kutta de 2ª ordem (RK2) e 4ª ordem (RK4)
# Script linear, sem definição de funções rk2/rk4

# Exemplo de problema:
#   y' = f(t, y)
#   y(0) = 0.8
# Aqui escolhemos: y' = y-t**2+1   (altere f se quiser outro problema)

f = lambda t, y: y-t**2+1  # <-- altere aqui para outro f(t,y)

# Parâmetros numéricos
t0 = 0.0      # tempo inicial
y0 = 0.5      # condição inicial
h  = 0.2      # passo
N  = 1       # número de passos (até t = t0 + N*h)

# Listas para armazenar as soluções
t_rk2 = [t0]
y_rk2 = [y0]

t_rk4 = [t0]
y_rk4 = [y0]

# ==========================
# Cálculo pelo RK2 (ponto médio)
# ==========================

t = t0
y = y0

for n in range(N):
    k1 = f(t, y)
    # ponto médio
    k2 = f(t + 0.5*h, y + 0.5*h*k1)

    # atualização
    y = y + h * k2
    t = t + h

    t_rk2.append(t)
    y_rk2.append(y)

# ==========================
# Cálculo pelo RK4 clássico
# ==========================

t = t0
y = y0

for n in range(N):
    k1 = f(t, y)
    k2 = f(t + 0.5*h, y + 0.5*h*k1)
    k3 = f(t + 0.5*h, y + 0.5*h*k2)
    k4 = f(t + h,     y + h*k3)

    y = y + (h/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)
    t = t + h

    t_rk4.append(t)
    y_rk4.append(y)

# ==========================
# Impressão dos resultados
# ==========================

print("t       RK2         RK4")
for i in range(len(t_rk2)):
    print(f"{t_rk2[i]:.2f}   {y_rk2[i]:.6f}   {y_rk4[i]:.6f}")
