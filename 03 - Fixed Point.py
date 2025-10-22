# Ache as raizes para a equação x^3+4x^2-10 = 0
import sys

# Escolhendo g(x)
g_x = lambda x: 1./2.*(10-x**3)**(1./2.)

p_0 = 1.5
tol = 10**(-3)
N = 1000

k = 1

while k<=N:
    p = g_x(p_0)
    if abs(p-p_0)<tol:
        print('A resposta é: ',p,' após',k,' iterações.')
        sys.exit()
    p_0 = p
    k+=k
print('Não foi possível achar a resposta.')
