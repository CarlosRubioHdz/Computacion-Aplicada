##### Programación básica #####
import numpy as np
import sys

# Solicitar dimensión de Matriz y validar

m=0
while m<3:
    m = int(input('Ingrese dimensión de matriz deseada: '))
    if m<3:
        print ("\n Por favor, ingrese un número igual o mayor a 3 \n")
        
# Elegir cantidad de números primos

n=m*m
primos=np.zeros((n,1))

primos[0]=2
prim=2
k=1

while k!=n:
    prim+=1
    deno=2
    residuo=1
    while residuo!=0:
        residuo=prim%deno
        if residuo==0 and prim==deno:
            primos[k]=prim
            k+=1
        deno+=1        

# Formación de la Matriz, imprimirla y realizar la suma

matriz=np.zeros((m,m))
k=0
suma=0
ma=""

print (f"\nLa matriz A de números primos consecutivos, de dimensión {m}, es: \n")
for i in range (m):
    for j in range (m):
        matriz[i,j]=primos[k]
        k+=1
        ma+=str(int(matriz[i,j]))+'\t'
        if i-j<=0:
            suma+=matriz[i,j]
    print (ma)
    ma=""

# Imprimir el resultado
print ("\n La suma de los elementos en la matriz es: ",int(suma))

