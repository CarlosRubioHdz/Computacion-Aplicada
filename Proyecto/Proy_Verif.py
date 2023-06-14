from matplotlib import pyplot as plt
from fitnessP import *

def Proy_Verif(R):
    #Resistor voltage measured/simulated data
    VR_data = [1.00E-07, 2.50E-02, 1.00E-01, 2.25E-01, 4.00E-01, 6.25E-01, \
                9.00E-01, 1.23E+00, 1.57E+00, 1.84E+00, 2.07E+00]
    #gate-to-source voltage sweep  
    VGS = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

    #fixed parameters
    Vin = 5         # Source Voltage 
    Vth = 0.69       #treshold voltage (for silicon)
    beta = 4.5e-6   #transistor's beta
    gamma=0.01				# 1/V
    Rsqt = 25        #sheet resistance, ohms per square

    #transistor variables
    W =R[0]        #gate width
    L =R[1]       #gate length
    print('W: '+str(round(1e6*W,1))+'μm\t'+'L: '+str(round(1e6*L,1))+'μm')

    #resistor
    m =R[2]           #resistor squares per line
    n =R[3]        #resistor lines        
    B=beta/2
    T=W/L
    R=Rsqt*((m*n)+(m-1))-(4*n/3)				# R(rsq, m, n)
    print("R:", R, 'Ω')

    #transistor's drain current I_D (for each V_GS value)
    #resistor voltage V_R = I_D * R
    VR = []
    for i in range(len(VGS)):
        if VGS[i] <= Vth:
            Vr = 0.0
        else:
            V=VGS[i]-Vth
            Vr = (1+gamma*Vin)/((1/(B*T*(V**2)*R))+gamma)
        VR.append(Vr)
    # mean square error
    MSE = fitnessP([W,L,m,n])

    print("mean sq error: ", round(MSE, 7))



    plt.figure(3)
    plt.plot(VGS,VR_data)
    plt.plot(VGS,VR)
    plt.grid()
    plt.legend(['Data','Calculated'])
    plt.title('$V_R$ vs $V_{GS}$')
    plt.ylabel('Resistor Voltage $[V]$')
    plt.xlabel('Gate-to-Source Voltage $[V]$')

    plt.show()
    
    return VR

