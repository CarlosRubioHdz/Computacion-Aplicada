import numpy as np

from normalizaP import *

def paretoP(pop,y,x):    
    #Normalizar
    [X,Y]=normalizaP(x,y)
        
    idealx=np.min(X)
    idealy=np.min(Y)
    
    dist=[]
    for i in range (0,len(pop)):
        d=((Y[i]-idealy)**2+(X[i]-idealx)**2)**(1/2)
        dist.append(d)
    dismin=np.min(dist)
    mejor_ind=dist.index(dismin)
    mejor=pop[mejor_ind]
    return mejor