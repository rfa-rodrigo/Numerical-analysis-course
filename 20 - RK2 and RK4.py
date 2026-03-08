# Método de Runge-Kutta de 2ª ordem (RK2) e 4ª ordem (RK4)
# Script linear, sem definição de funções rk2/rk4

# Exemplo de problema:
#   y' = f(t, y)
#   y(0) = 0.5
# Aqui escolhemos: y' = y-t**2+1   (altere f se quiser outro problema)
import math

f = lambda t, y: y-t**2+1  # <-- altere aqui para outro f(t,y)

real = lambda x: (x+1)**2-1/2*math.exp(x)

# Parâmetros numéricos
t0 = 0.0      # tempo inicial
y0 = 0.5      # condição inicial
h  = 0.2      # passo
N  = 100       # número de passos (até t = t0 + N*h)

# Listas para armazenar as soluções
t_rk1 = [t0]
y_rk1 = [y0]

t_rk2 = [t0]
y_rk2 = [y0]

t_rk3 = [t0]
y_rk3 = [y0]

t_rk4 = [t0]
y_rk4 = [y0]

# ==========================
# Cálculo pelo RK1
# ==========================

t = t0
y = y0

for n in range(N):
    k1 = h*f(t, y)
    
    y = y + k1
    t = t + h

    t_rk1.append(t)
    y_rk1.append(y)

# ==========================
# Cálculo pelo RK2
# ==========================

t = t0
y = y0

for n in range(N):
    k1 = h*f(t, y)
    k2 = h*f(t + 0.5*h, y + 0.5*k1)

    y = y + k2
    t = t + h

    t_rk2.append(t)
    y_rk2.append(y)

# ==========================
# Cálculo pelo RK3
# ==========================

t = t0
y = y0

for n in range(N):
    k1 = h*f(t, y)
    k2 = h*f(t + 0.5*h, y + 0.5*k1)
    k3 = h*f(t + h, y + 2*k2-k1)

    y = y + 1/6 * (k1 + 4*k2 + k3)
    t = t + h

    t_rk3.append(t)
    y_rk3.append(y)

# ==========================
# Cálculo pelo RK4 clássico
# ==========================

t = t0
y = y0

for n in range(N):
    k1 = h*f(t, y)
    k2 = h*f(t + 0.5*h, y + 0.5*k1)
    k3 = h*f(t + 0.5*h, y + 0.5*k2)
    k4 = h*f(t + h, y + k3)

    y = y + (1/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)
    t = t + h

    t_rk4.append(t)
    y_rk4.append(y)

# ==========================
# Impressão dos resultados
# ==========================

print("t       RK1         RK2         RK3         RK4         REAL")
for i in range(len(t_rk2)):
    print(f"{t_rk2[i]:.2f}  {y_rk1[i]:.6f}   {y_rk2[i]:.6f} {y_rk3[i]:.6f}  {y_rk4[i]:.6f}  {real(t_rk2[i]):.6f}")
