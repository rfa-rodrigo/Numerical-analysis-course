import sys
import math

# Funcão
f_x = lambda x: 2**x-3*abs(x)

k = 1
N = 300
tol = 0.05
a = 0
b = 1
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
  print(FP)

print("Nenhuma raiz foi encontrada")

