from gray2realP import*

def relacionP(pop):
    lambdaa=0.5*(10**-6)
    x=5*lambdaa
    rel=[]
    for i in range (0,len(pop)):
        mi=gray2realP(pop[i])[2]
        ni=gray2realP(pop[i])[3]
        ws=(ni*2*x)-x
        ls=(mi-1)*x
        if ws>=ls:
            rel.append(ws/ls)
        else:
            rel.append(ls/ws)
    return rel