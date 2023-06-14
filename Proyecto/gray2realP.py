# Convertir número Gray a uno binario a uno real

def gray2realP(indiv):
    lambdaa=0.5*(10**(-6))
    
    g1=indiv[0:6]		# Segmento de bits 0-9 <9=10-1>
    g2=indiv[6:11]		#w 1 o 2 bits más que L
    g3=indiv[11:16]		# L mayor a 2 lambda
    g4=indiv[16:21]
    
    b1=[g1[0]]
    b2=[g2[0]]
    b3=[g3[0]]
    b4=[g4[0]]
    
    for i in range (0,4):
        b2.append(int(b2[i]^g2[i+1]))	# el ^ indica el xor
        b3.append(int(b3[i]^g3[i+1]))
        b4.append(int(b4[i]^g4[i+1]))
    for i in range (0,5):
        b1.append(int(b1[i]^g1[i+1]))
        
    d1=0
    d2=0
    d3=0
    d4=0
    
    for i in range (len(b2)):
        d2+=b2[i]*2**(4-i)
        d3+=b3[i]*2**(4-i)
        d4+=b4[i]*2**(4-i)
    for i in range (len(b1)):        
        d1+=b1[i]*2**(5-i)
    
    
    W=(d1+4)*lambdaa
    L=(d2+2)*lambdaa
    m=d3+2
    n=d4+2
    
    R=[W,L,m,n]
    return R
        