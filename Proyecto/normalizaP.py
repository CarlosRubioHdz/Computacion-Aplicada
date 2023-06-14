import numpy as np

def normalizaP (x,y):
    xmin=np.min(x)
    xmax=np.max(x)
    ymin=np.min(y)
    ymax=np.max(y)
    
    X=[]
    Y=[]
    
    for i in range (0,len(x)):
        if xmax-xmin==0 or ymax-ymin==0:
            X.append((x[i]-xmin))
            Y.append((y[i]-ymin))
        else: 
            X.append((x[i]-xmin)/(xmax-xmin))
            Y.append((y[i]-ymin)/(ymax-ymin))
    
    return ([X,Y])