import sys

# Funcão
f_x = lambda x: x**3 + 4*x**2 - 10

k = 1
N = 300
tol = 10**(-8)
a = 1
b = 2
FA = f_x(a)

while k <= N:
  p = (a+b)/2
  FP = f_x(p)
  if (FP == 0) or (abs(FP)<tol):
    print("A raiz é: ",p)
    print("Foram necessárias: ",k," execuções.")
    sys.exit()
  if FA*FP>0:
    a = p
    FA = FP
  else:
    b = p
  k+=1

print("Nenhuma raiz foi encontrada")

