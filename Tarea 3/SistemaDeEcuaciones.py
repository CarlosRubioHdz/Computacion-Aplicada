##### Carlos Cristóbal Rubio Hernández    A01745245 #####

import numpy as np
import sys

print ("Una empresa fabrica dos productos, A y B. Cada producto tiene que ser \nprocesado por dos máquinas, I y II. Cada unidad del tipo A requiere \n1 hora de procesamiento de la máquina I y 1.5 horas por la máquina II \ny cada unidad del tipo B requiere de 3 horas en la máquina I y 2 horas \nen la máquina II. Si la máquina I está disponible 300 horas al mes y la \nmáquina II 350 horas, ¿cuántas unidades de cada tipo podrá fabricar al mes \nsi se utiliza el tiempo total del que dispone en las dos máquinas?")

# Definición de ecuaciones

# Producto A = x
# Producto B = y

# 1x+3y=300
# 1.5x+2y=350

# Matriz de Coeficientes

A=[[1,3],
   [1.5,2]]

# Matriz con los coeficientes de Igualación

B=[[300,350]]

detA=np.linalg.det(A)

n=len(A)

axd=np.zeros((n,n))
axdets=np.zeros((1,n))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if j==k:
                axd[i][j]=B[0][i]
            else:
                axd[i][j]=A[i][j]
    axdets[0][k]=np.linalg.det(axd)

res=np.zeros((1,n))
for k in range (n):
    res[0][k]=axdets[0][k]/detA

print(f"\n\nLa cantidad de productos a fabricar al mes:\n Producto A: {res[0,0]:.0f}\n Produco B: {res[0][1]:.0f}")

# Resolviendo con Numpy

a=np.array([[1,3],[1.5,2]])
b=np.array([300,350])

X=np.linalg.solve(a,b)

print("\n\nResolviendo con Numpy: ")
print(f"\n\nLa cantidad de productos a fabricar al mes:\n Producto A: {X[0]:.0f}\n Produco B: {X[1]:.0f}")
