# Evalúa el valor del voltaje

def voltajeP(R,vg):
    beta=4.5*10**-6			# A/V^2
    gamma=0.01				# 1/V
    Vth=0.69				# V
    W=R[0]
    L=R[1]
    m=R[2]
    n=R[3]
    Vin=5
    VGS=vg
    Rsqt=25					# Ohm
    
    # Cálculos para reducir
    B=beta/2
    T=W/L
    V=VGS-Vth
    R=Rsqt*((m*n)+(m-1))-(4*n/3)
    
    # Calcular Voltaje de la Resistencia
    if B*T*(V**2)*R==0:
        VR=100000
    else:
        VR=(1+gamma*Vin)/((1/(B*T*(V**2)*R))+gamma)
    
    return VR
