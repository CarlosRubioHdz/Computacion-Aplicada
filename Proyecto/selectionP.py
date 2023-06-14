import random
import numpy as np

def selectionP(fit):
    # Prioritizar menor error
    fit_=[]
    fitmax=np.max(fit)
    for i in range (0,len(fit)):
        fit_.append(fitmax-fit[i])

    total_fit=(sum(fit_))
    
    fit_index=0
    
    pick=random.random()	#número aleatorio entre 0 y 1
    fit_p=[]				#Proporción de aptitud respecto al total
    for i in range (0, len(fit)):
        fit_p.append((fit_[i]/total_fit))
    fit_acc=0
    for i in range (0,len(fit)):
        fit_acc+=fit_p[i]
        if fit_acc>=pick:
            fit_index=i
            break

    return fit_index
    