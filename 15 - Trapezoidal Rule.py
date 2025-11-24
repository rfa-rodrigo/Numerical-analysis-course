# Integração numérica pelo método dos trapézios (composto)

import math

# ------------------------------------------
# 1. DEFINIÇÃO DA FUNÇÃO E DO INTERVALO
# ------------------------------------------
# Edite aqui a função f(x), o intervalo [a, b] e o número de subintervalos n
f = lambda x: math.sin(x)  # exemplo de função
a = 0.0                    # limite inferior
b = math.pi                # limite superior
n = 10                     # número de subintervalos (inteiro >= 1)

# ------------------------------------------
# 2. CÁLCULO DO PASSO
# ------------------------------------------
h = (b - a) / n

# ------------------------------------------
# 3. APLICAÇÃO DA REGRA DO TRAPÉZIO COMPOSTA
#    Integral ≈ (h/2) * [f(x0) + 2*(f(x1)+...+f(x_{n-1})) + f(xn)]
# ------------------------------------------
soma = f(a) + f(b)   # f(x0) + f(xn)

# termos internos com peso 2
for i in range(1, n):
    x_i = a + i * h
    soma += 2.0 * f(x_i)

integral_aprox = (h / 2.0) * soma

print("Método dos trapézios (composto)")
print(f"Intervalo [{a}, {b}] com n = {n}")
print(f"Integral aproximada = {integral_aprox:.10f}")