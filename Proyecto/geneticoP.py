# Algoritmo Genético 3 Variables, 1 Función

import numpy as np
import matplotlib.pyplot as plt

from populationP import *
from new_indivP import *
from gray2realP import *
from fitnessP import *
from selectionP import *
from crossoverP import *
from mutationP import *
from voltajeP import *
from Proy_Verif import *
from relacionP import *
from dominaP import *
from paretoP import *

def geneticoP(n,c_len,tg):
#     # Crear población inicial

    pop=populationP(n,c_len)	# Población inicial
    bestfitg=[]
    
    for g in range (0,tg):
        fit= []
        for indiv in pop:
            fit.append(fitnessP(gray2realP(indiv)))

        fit_ind=selectionP(fit)
        parent0=pop[fit_ind]
        
        fit_ind=selectionP(fit)
        parent1=pop[fit_ind]

        z=0
        while parent1==parent0:
#             print ("estoy aquí")
            fit_ind=selectionP(fit)
            parent1=pop[fit_ind]
            z+=1
            if z==200:
                break

        offspring0, offspring1=crossoverP(parent0,parent1)	#Cruza
        
        offspring0=mutationP(offspring0)
        offspring1=mutationP(offspring1)
        
        #----------------------
        
        fitp0=fitnessP(gray2realP(parent0))
        fitp1=fitnessP(gray2realP(parent1))
        fito0=fitnessP(gray2realP(offspring0))
        fito1=fitnessP(gray2realP(offspring1))
        
        newpop=[]			#Nueva población (criterio personalizado)
        if fito0<=fitp0 or fito0<=fitp1:
            newpop.append(offspring0)
        if fito1<=fitp0 or fito1<=fitp1:
            newpop.append(offspring1)
        if fitp0<=fito0 and fito0<=fito1:
            newpop.append(parent0)
        if fitp1<=fito0 and fito1<=fito1:
            newpop.append(parent1)
          
        #juntar menor MSE por generación
        bestfit=np.min(fit)
        bestind=fit.index(bestfit)
        bestfitg.append(bestfit)
        
        # Relación Ws/Ls
        rela=relacionP(pop)
        
        # Elitismo original: incluye menor MSE de generación y MSE por debajo de la media-std_dev
        
#         newpop.append(pop[bestind])
#         
#         meanfit=np.mean(fit)
#         stddev_fit=np.std(fit)
#         for i in range(n):
#             if fit[i]<meanfit-stddev_fit:
#                 newpop.append(pop[i])
        
        # Elitismo multiobjetivo
            # Elitismo por no dominados
        nodomina=dominaP(pop,fit,rela)
        
        for i in range (0,len(nodomina)):
            newpop.append(nodomina[i])
        
        # Acompleta Población
        while len(newpop)<n:
            newpop.append(new_indivP(c_len))
        
        # No alterar última población para que coincida con fit
        if g<=tg-2:
            pop=newpop
        
    plt.figure(4)
    plt.plot(bestfitg)
    plt.title('Evolución de menor $MSE$ por generación')
    plt.ylabel('MSE')
    plt.xlabel('Generación')


# Elección original de mejor individuo
#     bestfit=np.min(fit)
#     bestindex=fit.index(bestfit)
#     sol=gray2realP(pop[bestindex])

# Elección de mejor individuo con distancia de pareto
    mejor_individuo=(paretoP(pop,fit,rela))
    sol=gray2realP(mejor_individuo)
    sol_ind=pop.index(paretoP(pop,fit,rela))
    rel_mejor=rela[sol_ind]
    fit_mejor=fit[sol_ind]
    
    solucion=[sol,mejor_individuo,fit_mejor,rel_mejor]

    return solucion
