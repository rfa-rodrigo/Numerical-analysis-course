import math

# Digite a função a ser integrada
integral = lambda x: x**3

# Digite 0 para aberto e 1 para fechado
intervalo = 0

# Escolha o intervalo a ser integrado
a = 0
b = 2

# Método (0, 1, 2 ou 3)
# 0 -> (Pendente) / ponto médio
# 1 -> trapézio / aberto 2 pontos
# 2 -> Simpson 1/3 / (Pendente)
n = 0

# Escolha a quantidade de subintervalos pares
N = 4

if intervalo == 0 :
    h = (b-a)/(N+2)
    pontos = lambda j: a+(1+j)*h
if intervalo == 1 :
    h = (b-a)/(N)
    pontos = lambda j: a+j*h

soma = 0.0

if (intervalo == 0) & (n == 0):
    for k in range(0,int(N/2)+1):
        calc = 2*h * (integral(pontos(2*k)))
        soma += calc

if (intervalo == 1) & (n==1):
    for k in range(1,N+1):
        calc = h/2*(integral(pontos(k-1))+integral(pontos(k)))
        soma += calc

if (intervalo == 1) & (n==2):
    for k in range(1,int(N/2)+1):
        calc = h/3 * (
                integral(pontos(2*k - 2)) +
                4*integral(pontos(2*k - 1)) +
                integral(pontos(2*k))
            )
        soma += calc

print(soma)