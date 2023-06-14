
def dominaP(pop,fit,rela):
    domina=[]
    for i in range (0,len(pop)):
        cond=0
        for j in range (0, len(pop)):
            if i!=j:
                if fit[i]>fit[j] and rela[i]>rela[j]:
                    cond+=1
        if cond==0:
            domina.append(pop[i])
    return domina

