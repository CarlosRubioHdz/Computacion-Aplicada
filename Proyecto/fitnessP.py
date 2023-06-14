# Evalúa aptitud del individuo , error cuadrático medio
from voltajeP import *

def fitnessP(R):
    #Resistor voltage measured/simulated data
    VR_data = [1.00E-07, 2.50E-02, 1.00E-01, 2.25E-01, 4.00E-01, 6.25E-01, \
            9.00E-01, 1.23E+00, 1.57E+00, 1.84E+00, 2.07E+00]
    #gate-to-source voltage sweep  
    VGS = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

    suma=0
    for i in range (0,len(VGS)):
        if VGS[i]<0.69:
            suma+=0
        else:
            suma+=(VR_data[i]-voltajeP(R,VGS[i]))**2
    
    error=(1/len(VGS))*suma
    
    return error
