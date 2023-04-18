# Carlos Cristóbal Rubio Hernández   A01745245
## Tarea 4: Integración Numérica
### Fórmula Compuesta de Simpson 3/8

import math
import numpy as np
import sys

def f(x):
#    f=math.exp(x**2)
#    f=1+(math.exp(-x)*math.sin(4*x))
#    f=math.sin(math.pi*x)
#    f=1+(math.exp(-x)*math.cos(4*x))
    f=math.sin(math.sqrt(x))
    return f

def sim38(a,b,n):
    h=(b-a)/n
    s=f(a)+f(b)
    for i in range (1,n):
        if i%3!=0:
            s=s+3*f(a+i*h)
        else:
            s=s+0
    for j in range (1,int(n/3)):
        s=s+2*f(a+3*j*h)
    S=(3/8)*h*s
    return S

def main():
    a=float(input("Ingrese límite inferior de integración: "))
    b=float(input("\nIngrese límite inferior de integración: "))
    n=2
    while n%3!=0:
        n=int(input("\nIngrese número de intervalos de integración: "))
        if n%3!=0:
            print ("\n\nEl valor de n debe de ser múltiplo de 3\n")
    Sim38=sim38(a,b,n)
    print(f"\nLa integración por método compuesto de Simpson 3/8 es: {Sim38:.7f}")

main()
