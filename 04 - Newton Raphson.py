# Ache as raizes para a equação x^3+4x^2-10 = 0
import sys

f_x = lambda x: x**3+4*x**2-10
f_prime = lambda x: 3*x**2+8*x

p_0 = 1.5
tol = 10**(-3)
N = 1000

k = 1

while k<=N:
    p = p_0-f_x(p_0)/f_prime(p_0)
    if abs(p-p_0)<tol:
        print('A resposta é: ',p,' após',k,' iterações.')
        sys.exit()
    p_0 = p
    k+=k
print('Não foi possível achar a resposta.')