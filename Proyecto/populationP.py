# Creación de Población

from new_indivP import *

def populationP(n,c_len):
    pop=[]
    for i in range (0,n):
        pop.append(new_indivP(c_len))
    return pop
