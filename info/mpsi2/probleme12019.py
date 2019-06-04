import numpy as np

# Filtrage du signal par un passe bas
def filtrage_passe_bas(freq,t,signal):
    tau = 1/freq # Coupure du filtre
    K=1
    res=[signal[0]]
    for i in range(1,len(signal)):
        h=t[i]-t[i-1]
        res.append((h*K*signal[i]+tau*res[-1])/(h+tau))
    return res

def dif(y,t):
    dy=np.copy(y)
    for k in range(len(y)-1):
        dy[k]=(y[k+1]-y[k])/(t[k+1]-t[k])
    dy[len(y)-1]=(y[-1]-y[-2])/(t[-1]-t[-2])
    return dy
    
#Filtrage du signal par une moyenne glissante
def filtrage_moyenne(signal,fenetre):
    filtrageg =signal[0:fenetre-1]
    for i in range(fenetre-1,len(signal)):
        s = sum(signal[i-fenetre+1:i+1])/fenetre
        filtrageg=np.concatenate([filtrageg,np.array([s])])
    return filtrageg 
    


#Q1
def recherche(m,s):
    """Recherche le mot m dans la chaîne s Préconditions : m et s sont des chaînes de caractères"""
    long_s = len(s)
    # Longueur de s
    long_m = len(m)
    # Longueur de m
    for i in range(long_s-long_m+1):
        # Invariant : m n'a pas été trouvé dans s[0:i+long_m-1]
        if s[i:i+long_m] == m:
            # On a trouvé m
            return True
    return False
    
#Q2
# with open('edt2018.gpx') as f:
#     data=f.readlines()
    
filename='edt2018.gpx'
with open(filename,'r') as f:
    data=f.readlines()
    lat=[]
    long=[]
    alt=[]
    tp=[]
    for ligne in data:
        if recherche('<trkpt',ligne)==True:
            l2=ligne.split('" lon="')
            l2[0]=l2[0].strip('<trkpt lat="')
            l2[1]=l2[1].strip('">\n')
            lat.append(float(l2[0]))
            long.append(float(l2[1]))
        elif recherche('<ele>',ligne)==True:
            l3=ligne.split('<ele>')
            l32=l3[1].strip('<ele>')
            l32=l32.strip('</ele>\n')
            alt.append(float(l32))
        elif recherche('<time>',ligne)==True:
            l4=ligne.split('<time>')
            lt=l4[1].strip('<time>')
            lt=lt.strip('</time>\n')
            lH=lt.split('T')[1]
            h,m,s=lH.split(':')
            if len(tp)==0:
                tp0=3600*float(h)+60*float(m)+float(s.strip('Z'))
            if len(alt)>0:
                tp.append(3600*float(h)+60*float(m)+float(s.strip('Z'))-tp0)

