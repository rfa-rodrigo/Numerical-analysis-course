import math

# ---------------------------------------------------------
# PARÂMETROS AJUSTÁVEIS PELO USUÁRIO
# ---------------------------------------------------------
a = 1.0      # limite inferior da integral
b = 3.0      # limite superior da integral
n = 2        # número de pontos de Gauss: 2 ou 3

# AQUI VOCÊ DEFINE A EXPRESSÃO DA FUNÇÃO f(x)
# Exemplo: f(x) = x**3 - 2*x + 1
# (basta alterar esta expressão dentro do laço mais abaixo)
# ---------------------------------------------------------

# Nós t_i e pesos w_i da quadratura de Gauss em [-1, 1]
if n == 2:
    t1 = -1.0 / math.sqrt(3.0)
    t2 =  1.0 / math.sqrt(3.0)

    w1 = 1.0
    w2 = 1.0

    ts = [t1, t2]
    ws = [w1, w2]

elif n == 3:
    t1 = -math.sqrt(3.0/5.0)
    t2 =  0.0
    t3 =  math.sqrt(3.0/5.0)

    w1 = 5.0/9.0
    w2 = 8.0/9.0
    w3 = 5.0/9.0

    ts = [t1, t2, t3]
    ws = [w1, w2, w3]

else:
    print("n deve ser 2 ou 3.")
    raise SystemExit

# Fator (b-a)/2 vindo de dx = (b-a)/2 dt
h = 0.5 * (b - a)

# Soma da quadratura: ∑ w_i f(x_i)
soma = 0.0
i = 0

while i < n:
    t = ts[i]
    w = ws[i]

    # MUDANÇA DE VARIÁVEL: x = ((b-a)*t + (a+b))/2
    x = 0.5 * ((b - a)*t + (a + b))

    # EXPRESSÃO DA FUNÇÃO f(x) (ajuste aqui quando quiser outra função)
    f_x = x**6 - x**2*math.sin(2*x)

    soma = soma + w * f_x
    i = i + 1

# Integral aproximada em [a,b]
integral_gauss = h * soma

print("Integral aproximada em [{:.6g}, {:.6g}] = {:.10g}".format(a, b, integral_gauss))
