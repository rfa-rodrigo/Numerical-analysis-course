import numpy as np
import sys

# Funcão
f_x = lambda x: 2*x**3 + 4*x**2 - 10*x - 10

# Derivada
f_prime = lambda x: 6*x**2 + 8*x - 10

# delta x na busca da continuidade da derivada
dx = 10**(-1)

# Intervalo
a = -2
b = 0

if f_x(a)*f_x(b) > 0:
  print("Não é possível afirmar sobre a existência de raízes no intervalo: [",a,",",b,"]")
  sys.exit()
if f_x(a)*f_x(b) < 0:
  if f_prime(a) <0:
      count = "negativo"
  if f_prime(a) >=0:
      count = "positivo"
  for k in np.arange(a,b,dx):
    if (f_prime(k) >= 0) and (count == "negativo"):
       print(f_prime(a), count)
       print('O intervalo possui raizes, mas não é possível afirmar que é somente uma')
       sys.exit()
    if (f_prime(k) < 0) and (count == "positivo"):
       print('O intervalo possui raizes, mas não é possível afirmar que é somente uma')
       sys.exit()
print('O intervalo possui uma única raiz')
