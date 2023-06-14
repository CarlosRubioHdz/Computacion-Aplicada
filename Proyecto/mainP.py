# Proyecto Final: Computación Aplicada
# Carlos Cristóbal Rubio Hernández

import numpy as np
import matplotlib.pyplot as plt

from geneticoP import *
from Proy_Verif import *

def main():
    c_len=21 				# tamaño de cromosoma, 4 genes
    
    # Datos para realizar el algoritmo
    print("*** Algoritmo Genético ***\n")
    n=int(input("Cantidad de individuos por generación: ")) 					# tamaño de la población
    print("Tamaño de cromosoma: \t", c_len,"bits")
    tg=int(input("Cantidad total de generaciones: "))							# total de generaciones
    veces=int(input("¿Cuantas veces desea realizar el algoritmo genético? "))
    
    datos=[]
    individuos=[]
    mse=[]
    relacion=[]
    for i in range (0,veces):
        gen=geneticoP(n,c_len,tg)
        datos.append(gen[0])
        individuos.append(gen[1])
        mse.append(gen[2])
        relacion.append(gen[3])
    
    lambdaa=0.5*(10**-6)
    x=5*lambdaa
    areas=[]
    for i in range (0,veces):
        Wi=datos[i][0]
        Li=datos[i][1]
        mi=datos[i][2]
        ni=datos[i][3]
        wsi=(ni*2*x)-x
        lsi=(mi-1)*x
        areai=((Wi*Li)+(wsi*lsi))*10**12
        areas.append(areai)
    
    mejor=(paretoP(individuos,mse,areas))
    individuo=individuos.index(mejor)
    
    sol=gray2realP(mejor)
    rel=relacion[individuo]
    ar=areas[individuo]
    ms=mse[individuo]
    [are_nor,mse_nor]=normalizaP(areas,mse)
    ar_nor=are_nor[individuo]
    ms_nor=mse_nor[individuo]
    
    print("\nm: ",sol[2],"\nn: ",sol[3])
    print("relacion: ",rel,"\tÁrea: ",round(ar,3),"μm^2")
    
    plt.figure(1)
    plt.scatter(x=areas,y=mse)
    plt.scatter(x=ar,y=ms)
    plt.legend(['Mejores Individuos','Elección'])
    plt.title('MSE vs Área')
    plt.ylabel('$MSE$')
    plt.xlabel('Área $[μm^2]$')
    
    plt.figure(2)
    plt.scatter(x=are_nor,y=mse_nor)
    plt.scatter(x=ar_nor,y=ms_nor)
    plt.legend(['Mejores Individuos','Elección'])
    plt.title('MSE vs Área (Normalizado)')
    plt.ylabel('$MSE$ (Normalizado)')
    plt.xlabel('Área (Normalizado)')
    
    Proy_Verif(sol)

main()
    