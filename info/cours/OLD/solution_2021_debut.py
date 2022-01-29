import matplotlib.pyplot as plt
import numpy as np
import os

filename='mont_dor.gpx'
filename='rumilly.gpx'
filename='trace1.gpx'


def recherche(m,s):
    """Recherche le mot m dans la chaîne s
    Préconditions : m et s sont des chaînes de caractères"""
    long_s = len(s) # Longueur de s
    long_m = len(m) # Longueur de m
    for i in range(long_s-long_m):
        # Invariant : m n’a pas été trouvé dans s[0:i+long_m-1]
        if s[i:i+long_m] == m: # On a trouvé m
            return True
    return False

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


#Superposition sur une carte 
import folium
macarte = folium.Map(location=[(max(lat)+min(lat))/2,(min(long)+max(long))/2], zoom_start=13)
points=[]
for k in range(len(lat)):
    points.append(tuple([lat[k],long[k]]))
folium.PolyLine(points).add_to(macarte)
macarte.save('carte.html')

#Ouverture de firefox
#os.system('/Applications/Firefox.app/Contents/MacOS/firefox -new-tab test.html')


                #Derivation numérique
def dif(y,t):
    dy=np.copy(y)
    for k in range(len(y)-1):
        dy[k]=(y[k+1]-y[k])/(t[k+1]-t[k])
    dy[len(y)-1]=(y[-1]-y[-2])/(t[-1]-t[-2])
    return dy
 
R=6371*1E3 
r=R+np.array(alt)  
phi=np.array(long)
theta=90-np.array(lat) 
 
 
    
plt.clf()
plt.figure(figsize=(20,10))
plt.title('Dérivée temporelle des coordonnees sphériques')
plt.subplot(1,3,1)
plt.plot(tp,dif(r,tp))
plt.xlabel('temps (s)')
plt.ylabel('$\dot{r}(t)$ (en m/s)')
plt.subplot(1,3,2)
plt.plot(tp,dif(theta,tp))
plt.xlabel('temps (s)')
plt.ylabel('$\dot{\\theta}(t)$ (en $^{\\circ}$/s)')
plt.subplot(1,3,3)
plt.plot(tp,dif(phi,tp))
plt.xlabel('temps (s)')
plt.ylabel('$\dot{\\varphi}(t)$ (en $^{\\circ}$/s)')
plt.savefig('der_coor_sph.png')


# Filtrage du signal par un passe bas
def filtrage_passe_bas(freq,t,signal):
    tau = 1/freq # Coupure du filtre
    K=1
    res=[signal[0]]
    for i in range(1,len(signal)):
        h=t[i]-t[i-1]
        res.append((h*K*signal[i]+tau*res[-1])/(h+tau))
    return res


    
#Filtrage du signal par une moyenne glissante
def filtrage_moyenne(signal,fenetre):
    filtrageg =signal[0:fenetre-1]
    for i in range(fenetre-1,len(signal)):
        s = sum(signal[i-fenetre+1:i+1])/fenetre
        filtrageg=np.concatenate([filtrageg,np.array([s])])
    return filtrageg


#flitrage des donnees
#Etude parametrique du filtrage
plt.clf()
plt.figure(figsize=(20,10))
plt.title('Etude parametrique du filtrage')
plt.subplot(1,2,1)
plt.plot(tp,r,label="signal brut")
vfreq=[1,1/10,1/30,1/60]
for freq in vfreq:
    rf=filtrage_passe_bas(freq,tp,r)
    plt.plot(tp,rf,label="Passe bas avec freq="+str(round(freq,2)))
plt.xlabel('temps (s)')
plt.ylabel('$r$ (en m)')
plt.legend(loc=0)
plt.subplot(1,2,2)
plt.plot(tp,r,label="signal brut")
vfren=[1,3,10,20]
for fenetre in vfren:
    rf2=filtrage_moyenne(r,fenetre)
    plt.plot(tp,rf2,label="moyenne glissante avec fenetre="+str(fenetre))
plt.xlabel('temps (s)')
plt.ylabel('$r$ (en m)')
plt.legend(loc=0)

plt.savefig('para_flt.png')
#Filtrage pour le calcul de la puissance
freq=1/20
rf=filtrage_passe_bas(freq,tp,r) 
thetaf=filtrage_passe_bas(freq,tp,theta) 
phif=filtrage_passe_bas(freq,tp,phi)
fenetre=10
rf2=filtrage_moyenne(r,fenetre) 
thetaf2=filtrage_moyenne(theta,fenetre) 
phif2=filtrage_moyenne(phi,fenetre)  
    
plt.clf()
plt.figure(figsize=(20,10))
plt.title('Coordonnees sphériques au cours du temps')
plt.subplot(1,3,1)
plt.plot(tp,r,label="signal brut")
plt.plot(tp,rf,label="filtre passe bas")
plt.plot(tp,rf2,label="moyenne glissante")
plt.xlabel('temps (s)')
plt.ylabel('$r$ (en m)')
plt.legend(loc=0)
plt.subplot(1,3,2)
plt.plot(tp,theta,label="signal brut")
plt.plot(tp,thetaf,label="filtre passe bas")
plt.plot(tp,thetaf2,label="moyenne glissante")
plt.xlabel('temps (s)')
plt.ylabel('$\\theta(t)$ (en $^{\\circ}$)')
plt.legend(loc=0)
plt.subplot(1,3,3)
plt.plot(tp,phi,label="signal brut")
plt.plot(tp,phif,label="filtre passe bas")
plt.plot(tp,phif2,label="moyenne glissante")
plt.xlabel('temps (s)')
plt.ylabel('$\\varphi(t)$ (en $^{\\circ}$)')
plt.legend(loc=0)
plt.savefig('coor_sph_flt.png')


plt.clf()
plt.figure(figsize=(20,10))
plt.title('Dérivée temporelle des coordonnees sphériques')
plt.subplot(1,3,1)
plt.plot(tp,dif(r,tp),label="signal brut")
plt.plot(tp,dif(rf,tp),label="filtre passe bas")
#plt.plot(tp,dif(rf2,tp),label="moyenne glissante")
plt.xlabel('temps (s)')
plt.ylabel('$\dot{r}(t)$ (en m/s)')
plt.legend(loc=0)
plt.subplot(1,3,2)
plt.plot(tp,dif(theta,tp),label="signal brut")
plt.plot(tp,dif(thetaf,tp),label="filtre passe bas")
#plt.plot(tp,dif(thetaf2,tp),label="moyenne glissante")
plt.xlabel('temps (s)')
plt.ylabel('$\dot{\\theta}(t)$ (en $^{\\circ}$/s)')
plt.legend(loc=0)
plt.subplot(1,3,3)
plt.plot(tp,dif(phi,tp),label="signal brut")
plt.plot(tp,dif(phif,tp),label="filtre passe bas")
#plt.plot(tp,dif(phif2,tp),label="moyenne glissante")
plt.xlabel('temps (s)')
plt.ylabel('$\dot{\\varphi}(t)$ (en $^{\\circ}$/s)')
plt.legend(loc=0)
plt.savefig('der_coor_sph_flt.png')


#Calcul des vitesses et acceleration

def vitesse(r,theta,phi,t):
    """renvoie le vecteur vitesse en coordonnee spherique a chaque instant et sa norme V"""
    vr=dif(r,t)
    vtheta=r*dif(theta*np.pi/180,t)
    vphi=r*np.sin(theta*np.pi/180)*dif(phi*np.pi/180,t)
    V=np.sqrt(vr**2+vtheta**2+vphi**2)
    return vr,vtheta,vphi,V
    
def acceleration(r,theta,phi,t):
    """renvoie le vecteur acceleration en coordonnee spherique a chaque instant et sa norme V"""
    rp=dif(r,t)
    rpp=dif(rp,t)
    thetap=dif(theta,t)*np.pi/180
    thetapp=dif(thetap,t)
    phip=dif(phi,t)*np.pi/180
    phipp=dif(phip,t)
    ar=rpp-r*thetap**2-r*(np.sin(theta*np.pi/180))**2*phip**2
    atheta=2*rp*thetap+r*thetapp-r*np.sin(theta*np.pi/180)*np.cos(theta*np.pi/180)*phip**2
    aphi=2*r*np.cos(theta*np.pi/180)*thetap*phip+2*rp*phi*np.sin(theta*np.pi/180)+r*np.sin(theta*np.pi/180)*phipp
    a=np.sqrt(ar**2+atheta**2+aphi**2)
    return ar,atheta,aphi,a

(vr1,vtheta1,vphi1,V1)=vitesse(r,theta,phi,tp)
(vr2,vtheta2,vphi2,V2)=vitesse(np.array(rf),np.array(thetaf),np.array(phif),tp)
(vr3,vtheta3,vphi3,V3)=vitesse(np.array(rf2),np.array(thetaf2),np.array(phif2),tp)
(ar1,atheta1,aphi1,a1)=acceleration(r,theta,phi,tp)
(ar2,atheta2,aphi2,a2)=acceleration(np.array(rf),np.array(thetaf),np.array(phif),tp)
(ar3,atheta3,aphi3,a3)=acceleration(np.array(rf2),np.array(thetaf2),np.array(phif2),tp)
plt.clf()
plt.figure(figsize=(20,10))
plt.title('Affichage de la vitesse et de l accélération')
plt.subplot(2,2,1)
plt.plot(tp,V1,label="signal brut")
plt.plot(tp,V2,label="filtre passe bas")
#plt.plot(tp,V3,label="moyenne glissante")
plt.xlabel('temps (s)')
plt.ylabel('$V$ (en m/s)')
plt.legend(loc=0)
plt.subplot(2,2,2)
#plt.plot(tp,dif(V1,tp))
plt.plot(tp,dif(V2,tp),label="filtre passe bas")
#plt.plot(tp,V3,label="moyenne glissante")
plt.xlabel('temps (s)')
plt.ylabel('$a$ (en m/s2)')
plt.subplot(2,2,3)
plt.plot(tp,r)
plt.xlabel('temps (s)')
plt.ylabel('$r$ (en m)')
plt.subplot(2,2,4)
plt.plot(tp,r)
plt.xlabel('temps (s)')
plt.ylabel('$r$ (en m)')

plt.savefig('V-A.png')


#Estimation de la distance parcouru
def trapeze(f,t):
    I=0
    vI=[I]
    for k in range(1,len(t)):
        I+=(t[k]-t[k-1])*(f[k]+f[k-1])*0.5
        vI.append(I)
    return I,vI
    
d



    