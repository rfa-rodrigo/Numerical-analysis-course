# Integração numérica pelo método de Simpson 1/3 (composto)

import math

# ------------------------------------------
# 1. DEFINIÇÃO DA FUNÇÃO E DO INTERVALO
# ------------------------------------------
# Edite aqui a função f(x), o intervalo [a, b] e o número de subintervalos n
f = lambda x: math.sin(x)  # exemplo de função
a = 0.0                    # limite inferior
b = math.pi                # limite superior
n = 10                     # número de subintervalos (PRECISA ser par)

if n % 2 != 0:
    raise ValueError("Para Simpson 1/3 composto, o número de subintervalos n deve ser par.")

# ------------------------------------------
# 2. CÁLCULO DO PASSO
# ------------------------------------------
h = (b - a) / n

# ------------------------------------------
# 3. APLICAÇÃO DA REGRA DE SIMPSON 1/3 COMPOSTA
#    Integral ≈ (h/3) * [f(x0) + f(xn)
#                        + 4*(f(x1)+f(x3)+...+f(x_{n-1}))
#                        + 2*(f(x2)+f(x4)+...+f(x_{n-2}))]
# ------------------------------------------
soma = f(a) + f(b)

# termos com coeficiente 4 (índices ímpares)
for i in range(1, n, 2):
    x_i = a + i * h
    soma += 4.0 * f(x_i)

# termos com coeficiente 2 (índices pares, exceto extremos)
for i in range(2, n, 2):
    x_i = a + i * h
    soma += 2.0 * f(x_i)

integral_aprox = (h / 3.0) * soma

print("Método de Simpson 1/3 (composto)")
print(f"Intervalo [{a}, {b}] com n = {n}")
print(f"Integral aproximada = {integral_aprox:.10f}")