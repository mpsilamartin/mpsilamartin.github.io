import datetime
import os, glob
import sqlite3
import pandas as pd

#RAZ du fichier log
f=open('log.txt','w')

conn=sqlite3.connect('mpsi_quizz.db')
c=conn.cursor()


#Mise à 0 des scores
req_etudiants="select nom, prenom from etudiants"
c.execute(req_etudiants)
for l in c.fetchall():
    (nom,prenom)=l
    req_raz1="update etudiants set score_cumule="+str(0)+" where nom='"+nom+"' and prenom='"+prenom+"'"
    c.execute(req_raz1)
    req_raz2="update etudiants set classement="+str(11)+" where nom='"+nom+"' and prenom='"+prenom+"'"
    c.execute(req_raz2)
    req_raz3="update etudiants set evol_classement="+str(0)+" where nom='"+nom+"' and prenom='"+prenom+"'"
    c.execute(req_raz3)
    
conn.commit()
conn.close()