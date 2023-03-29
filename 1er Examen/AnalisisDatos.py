##### Análisis de Datos #####

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
import math
import sys


# Importar los Datos

data0 = np.loadtxt("EstadisticaTallas.txt", dtype=str)

#Extraer los datos independientes de Estatura, Talla de Calzado y Género

n=len(data0)
Estatura=np.zeros((n,1))
for i in range (n):
    Estatura[i][0]=int(data0[i][0])

Talla=np.zeros((n,1))
for i in range (n):
    Talla[i][0]=float(data0[i][1])
    
Genero=[]
for i in range (n):
    Genero.append(data0[i][2])
#Obtención de la Media y de la Desviación Estandar de ambos datos

MuEstatura=np.mean(Estatura)
MuTalla=np.mean(Talla)

StdEstatura=np.std(Estatura)
StdTalla=np.std(Talla)

# Distribución Normal

def distribucion_normal(xi,Mu,Sigma):
    return np.exp(-1*((xi-Mu)**2)/(2*(Sigma**2)))/(math.sqrt(2*np.pi)*Sigma)

xEst=np.linspace(75,250,1000)
DNEstatura=distribucion_normal(xEst,MuEstatura,StdEstatura)
xTalla=np.linspace(15,35,100)
DNTalla=distribucion_normal(xTalla,MuTalla,StdTalla)

# Cálculo de Probabilidad

ProbaEsta1=norm(loc=MuEstatura,scale=StdEstatura).cdf(MuEstatura)
ProbaEsta2=norm(loc=MuEstatura,scale=StdEstatura).cdf(MuEstatura-StdEstatura)
ProbaEsta=(ProbaEsta1-ProbaEsta2)*100

ProbaTalla1=norm(loc=MuTalla,scale=StdTalla).cdf(MuTalla)
ProbaTalla2=norm(loc=MuTalla,scale=StdTalla).cdf(MuTalla-StdTalla)
ProbaTalla=(ProbaTalla1-ProbaTalla2)*100

# Aproximación lineal de la Relación Estatura vs Talla de Calzado. Población General

sx = sum (Talla) 
sy = sum (Estatura)

x2 = []
for i in Talla:
    x2.append(i*i)


xy = []
for i in range(0,n):
    val=Talla[i]*Estatura[i]
    xy.append(val)
 
sx2 = sum(x2)
sxy = sum(xy)
 
m = float((n*sxy-sx*sy)/(n*sx2-sx*sx))
b = float((sy*sx2-sx*sxy)/(n*sx2-sx*sx))

ym = []
for i in Talla:
    ye=m*i+b
    ym.append(ye)

# Aproximación lineal de la Relación Estatura vs Talla de Calzado. Hombres y Mujeres

EstaturaH=[]
EstaturaM=[]
TallaH=[]
TallaM=[]

for i in range (n):
    if Genero[i]=="Masculino":
        EstaturaH.append(Estatura[i])
        TallaH.append(Talla[i])
    elif Genero[i]=="Femenino":
        EstaturaM.append(Estatura[i])
        TallaM.append(Talla[i])
        
nH=len(EstaturaH)
nM=len(EstaturaM)

sxH = sum (TallaH) 
syH = sum (EstaturaH)
sxM = sum (TallaM) 
syM = sum (EstaturaM)

x2H = []
for i in TallaH:
    x2H.append(i*i)
x2M = []
for i in TallaM:
    x2M.append(i*i)

xyH = []
for i in range(0,nH):
    valH=TallaH[i]*EstaturaH[i]
    xyH.append(valH)
xyM = []
for i in range(0,nM):
    valM=TallaM[i]*EstaturaM[i]
    xyM.append(valM)
 
sx2H = sum(x2H)
sxyH = sum(xyH)
sx2M = sum(x2M)
sxyM = sum(xyM)
 
mH = float((nH*sxyH-sxH*syH)/(nH*sx2H-sxH*sxH))
bH = float((syH*sx2H-sxH*sxyH)/(nH*sx2H-sxH*sxH))
mM = float((nM*sxyM-sxM*syM)/(nM*sx2M-sxM*sxM))
bM = float((syM*sx2M-sxM*sxyM)/(nM*sx2M-sxM*sxM))

ymH = []
for i in TallaH:
    ye=mH*i+bH
    ymH.append(ye)
ymM = []
for i in TallaM:
    ye=mM*i+bM
    ymM.append(ye)

# Impresión de Datos Solicitados

print(f"El valor de la Media (Mu) para los datos de Estatura es de: \n{MuEstatura:.2f} [cm]")
print(f"\nEl valor de la Desviación Estandar (Sigma) para los datos de Estatura es de: \n{StdEstatura:.2f} [cm]")
print(f"\n\nEl valor de la Media (Mu) para los datos de Talla de Calzado es de: \n{MuTalla:.2f} [cm]")
print(f"\nEl valor de la Desviación Estandar (Sigma) para los datos de Talla de Calzado es de: \n{StdTalla:.2f} [cm]")

print(f"\n\nLa probabilidad de que una persona tomada al azar se encuentre dentro \nde la primera Desviación Estándar, es decir, el área entre \nMedia-Desviación Estándar (Mu-Sigma) y la Media (Mu), para Estatura \nes de: {ProbaEsta:.3f}%")
print(f"\nLa probabilidad de que una persona tomada al azar se encuentre dentro \nde la primera Desviación Estándar, es decir, el área entre \nMedia-Desviación Estándar (Mu-Sigma) y la Media (Mu), para \nTalla de Calzado es de: {ProbaTalla:.3f}%")

print(f"\n\nLa aproximación lineal, de forma 'y=mx+b', que describe la relación \nentre Estatura y Talla de Calzado para la Población General es: \ny={m:.3f}x+{b:.3f}")
print(f"\nLa aproximación lineal que describe la relación \nentre Estatura y Talla de Calzado para la Población de Hombres es: \ny={mH:.3f}x+{bH:.3f}")
print(f"\nLa aproximación lineal que describe la relación \nentre Estatura y Talla de Calzado para la Población de Mujeres es: \ny={mM:.3f}x+{bM:.3f}")

# Realización de los Gráficos solicitados

plt.figure("Distribución Normal 1")
plt.title("Estatura")
plt.plot(xEst,DNEstatura)
plt.xlabel('Estatura [cm]')
plt.grid()

plt.figure("Distribución Normal 2")
plt.title("Talla de Calzado")
plt.plot(xTalla,DNTalla)
plt.xlabel('Talla calzado [cm]')
plt.grid()

clases1 = 15
rango1 = (87,193.5)
plt.figure("Histograma 1")
plt.title("Estatura")
plt.xlabel("Estatura [cm]")
plt.ylabel("Cantidad")
plt.hist(Estatura, range=rango1, bins = clases1, density=False)

clases2 = 15
rango2 = (20,35)
plt.figure("Histograma 2")
plt.title("Talla de Calzado")
plt.xlabel("Talla de Calzado [cm]")
plt.ylabel("Cantidad")
plt.hist(Talla, range=rango2, bins = clases2, density=False)

plt.figure("Aproximación Lineal")
plt.plot(Talla,Estatura,'o', label='Estatura(Talla)')
plt.plot(Talla,ym, label='Estatura_media')
plt.title("Relación Estatura vs Talla")
plt.xlabel("Talla de Calzado [cm]")
plt.ylabel("Estatura [cm]")
plt.legend()

plt.figure("Aproximación Lineal 2")
plt.plot(TallaH,EstaturaH,'o', label='EstaturaH(TallaH)')
plt.plot(TallaH,ymH, label='EstaturaH_media')
plt.xlabel("Talla de Calzado [cm]")
plt.ylabel("Estatura [cm]")
plt.legend()

plt.figure("Aproximación Lineal 2")
plt.plot(TallaM,EstaturaM,'o', label='EstaturaM(TallaM)')
plt.plot(TallaM,ymM, label='EstaturaM_media')
plt.title("Relación Estatura vs Talla Dividido por Sexo")
plt.xlabel("Talla de Calzado [cm]")
plt.ylabel("Estatura [cm]")
plt.legend()

plt.show()
