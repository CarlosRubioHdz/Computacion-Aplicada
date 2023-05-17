import numpy as np
import math
from random import random
from random import gauss
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def f(x1,x2,x3):
    #f = (4-2.1*(x**2)+((x**4)/3))*(x**2)+(x*y)+(-4+4*(y**2))*(y**2)
    #f = x**2+y**2
    f=x1+2*x2+x2*x3-x1**2-x2**2-x3**2
    return f

def path(u,v,w):
    fig=plt.figure(1)
    axes=plt.axes(projection='3d')
    axes.scatter(u[0],v[0],w[0],c='b',marker='o')
     
    for i in range (0,len(u)-1):
        plt.plot([u[i],u[i+1]],[v[i],v[i+1]],[w[i],w[i+1]],'r+-')
    
    axes.scatter(u[-1],v[-1],w[-1],c='black',marker='s')
    
    plt.plot(1/2, 4/3,2/3, 'gx')
    
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xlabel("x1")
    plt.ylabel('x2')
    axes.set_zlabel('x3')
    plt.grid()
    plt.title('Trayectoria de la evolución');
       
    #plt.show()

def mutation (x,s):
    xn=x+s*gauss(0,1)
    while xn<-2 or xn>2:
        xn=x+s*gauss(0,1)
    return xn

def sigma(s,g,m):
    ps=m/g
    c=0.817
    if g%20==0:
        if ps>0.2:
            s=s/c
        else:
            s=s*c
    else:
        s=s
    return s

def evol(u,v,w):
    plt.figure(2)
    x_1=[]
    x_2=[]
    x_3=[]
    for i in range(len(u)):
        x_1.append(1/2)
        x_2.append(4/3)
        x_3.append(2/3)
    plt.plot(u,'blue')
    plt.plot(v,'green')
    plt.plot(w,'red')
    plt.plot(x_1,'yellow')
    plt.plot(x_2,'yellow')
    plt.plot(x_3,'yellow')
    plt.legend(('x1','x2','x3'))
    plt. ylim([-2,2])
    plt.xlabel('Generación')
    plt.ylabel('Valor de Variable')
    plt.title('Evolución de las Variables')
    plt.grid()
    plt.show()
    
def main():
    #Parámetros
    xmin, xmax= [-2,2]
    gmax=500
    m=0
    
    #individuo inicial
    x1=4*random()+xmin
    x2=4*random()+xmin
    x3=4*random()+xmin
    
    x10x20x30=[round(x1,6),round(x2,6),round(x3,6)]
    print("x1_0,x2_0, x3_0: ",x10x20x30)
    
    #primer padre
    padre=f(x1,x2,x3)
    
    s=1
    
    #Registro de individuos
    u=[x1]
    v=[x2]
    w=[x3]
    
    for g in range(1,gmax):
        x1n=mutation(x1,s)
        x2n=mutation(x2,s)
        x3n=mutation(x3,s)
        hijo=f(x1n,x2n,x3n)
        if hijo>padre:
            x1=x1n
            x2=x2n
            x3=x3n
            m+=1
            padre=f(x1,x2,x3)
        else:
            x1=x1
            x2=x2
            x3=x3
            m=m
        s=sigma(s,g,m)
        u.append(x1)
        v.append(x2)
        w.append(x3)
    x1fx2fx3f=[round(x1,6),round(x2,6),round(x3,6)]
    print("x1f,x2f, x3f: ",x1fx2fx3f)    
    
    path(u,v,w)
    evol(u,v,w)
    
main()