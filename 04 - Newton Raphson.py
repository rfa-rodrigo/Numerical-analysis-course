# Ache as raizes para a equação x^3+4x^2-10 = 0
import sys
import math

f_x = lambda x: x-2*math.sin(x)
f_prime = lambda x: 1-2*math.cos(x)

p_0 = 1.7
tol = 0.001
N = 1000

k = 1

while k<=N:
    p = p_0-f_x(p_0)/f_prime(p_0)
    if abs(p-p_0)<tol:
        print('A resposta é: ',p,' após',k-1,' iterações.')
        sys.exit()
    p_0 = p
    k+=k
    print(p)
print('Não foi possível achar a resposta.')