from math import log

alpha=100

def generer_altitude(alpha):
    alt0= [300, 500, 600, 1000, 800, 900, 500, 600, 200, 0]
    alt0=(alpha%4+1)*alt0
    alt0=alt0[alpha%3:-1-alpha%2]
    alt=[]
    for i,x in enumerate(alt0):
        delta=(-1)**i*((alpha+i%3)*739)%79
        alt.append(x+delta)
    return alt

alt=generer_altitude(alpha)