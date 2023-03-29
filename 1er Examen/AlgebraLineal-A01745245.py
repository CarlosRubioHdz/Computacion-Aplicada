##### Álgebra Lineal #####

import numpy as np
import sys

print ("Una planta de fertilizantes produce tres tipos de fertilizantes.\n\nEl tipo A contiene 25% de potasio, 45% de nitrato y 30% de fosfato.\nEl tipo B contiene 15% de potasio, 50% de nitrato y 35% de fosfato.\nEl tipo C no contiene potasio, tiene 75% de nitrato y 25% de fosfato.\n\nLa planta tiene suministros de 1.5 toneladas diarias de potasio,\n5 toneladas al día de nitrato y de 3 toneladas al día de fosfato.\n\n¿Qué cantidad de cada tipo de fertilizante deberá producir de modo que\nagote los suministros de ingredientes?")

# Definición de ecuaciones

# Tipo A = x
# Tipo B = y
# Tipo C = z

# 0.25x+0.15y+0.00z=1.5T
# 0.45x+0.50y+0.75z=5T
# 0.30x+0.35y+0.25z=3T

# Matriz de Coeficientes

A=[[0.25,0.15,0.00],
   [0.45,0.5,0.75], 
   [0.30,0.35,0.25]]

# Matriz con los coeficientes de Igualación

B=[[1.5,5,3]]

detA=np.linalg.det(A)

axd=np.zeros((3,3))
axdets=np.zeros((1,3))

for k in range(3):
    for i in range(3):
        for j in range(3):
            if j==k:
                axd[i][j]=B[0][i]
            else:
                axd[i][j]=A[i][j]
    axdets[0][k]=np.linalg.det(axd)

res=np.zeros((1,3))
for k in range (3):
    res[0][k]=axdets[0][k]/detA

print(f"\n\nCantidad en Toneladas a producir de fertilizante: \n  Tipo A = {res[0][0]:.3f} \n  Tipo B = {res[0][1]:.3f} \n  Tipo C = {res[0][2]:.3f}")

# Resolviendo con Numpy

a=np.array([[0.25,0.15,0.00],[0.45,0.5,0.75],[0.30,0.35,0.25]])
b=np.array([1.5,5,3])

X=np.linalg.solve(a,b)

print("\n\nResolviendo con Numpy: ")
print(f"\nCantidad en Toneladas a producir de fertilizante: \n  Tipo A = {X[0]:.3f} \n  Tipo B = {X[1]:.3f} \n  Tipo C = {X[2]:.3f}")
