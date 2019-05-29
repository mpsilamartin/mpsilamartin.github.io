# -*- coding: utf-8 -*
#Installation du module xlutils
#pip install xlutils
import numpy as np
import xlrd
import datetime
import os, glob
import sqlite3
import pandas as pd

#RAZ du fichier log
f=open('log.txt','w')

conn=sqlite3.connect('mpsi_quizz.db')
c=conn.cursor()


liste_quizz=['C4','C4-2']#Liste des quiz à traiter pour la modification de la bdd
liste_quizz=['C7-1']#Liste des quiz à traiter pour la modification de la bdd
liste_quizz=['C8-1-1','C8-1-2']#Liste des quiz à traiter pour la modification de la bdd

#Mise à 0 des scores
req_etudiants="select nom, prenom from etudiants"
c.execute(req_etudiants)
for l in c.fetchall():
    (nom,prenom)=l
    req_raz1="update etudiants set score_cumule="+str(0)+" where nom='"+nom+"' and prenom='"+prenom+"'"
    c.execute(req_raz1)
    req_raz2="update etudiants set classement="+str(11)+" where nom='"+nom+"' and prenom='"+prenom+"'"
    c.execute(req_raz1)

for q in liste_quizz:
    #Determination des donnees du quiz
    c.execute("SELECT idquiz, nbr_question FROM quiz WHERE nom_quiz='"+q+"'")
    (id_quiz,nbr_question)=c.fetchone()
    path=r"/Users/emiliendurif/Documents/prepa/MPSI/site/mpsilamartin.github.io/sii/mpsi2/mpsi_quiz/"+q+".xlsx"
    classeur=xlrd.open_workbook(path)
    feuilles=classeur.sheet_names()
    #Ouverture de la feuille du quiz
    for f in feuilles:
        if "Sheet1" in f:
            fs=classeur.sheet_by_name(f)
        
    #Detection de la premier ligne
    i=0
    while 'Student' not in fs.cell_value(i,0):
        i+=1
    i+=1
    #i indice de la premiere ligne de donnee
    #Balayage des lignes de donnees
    while 'Class' not in fs.cell_value(i,0):
        nom=fs.cell_value(i,0)
        score=fs.cell_value(i,3)
        c.execute("SELECT idetudiant FROM etudiants WHERE lower(Nom)=lower('"+nom+"')")
        idetudiant=c.fetchone()
        print(idetudiant)
        c.execute("INSERT INTO joue (idetudiant,idquiz,score) VALUES ("+str(idetudiant[0])+","+str(id_quiz)+","+str(score)+")")
        i+=1
        #c.fetchone()
    #Requete pour afficher le score cumule
    req_score="select nom, prenom, sc_total from (select nom, prenom, sum(score) as sc_total from (select nom, prenom, score from etudiants join joue on etudiants.idetudiant=joue.idetudiant) group by nom) order by sc_total DESC"
    c.execute(req_score)
    for l in c.fetchall():
        (nom,prenom,sc_total)=l
        req_update="update etudiants set score_cumule="+str(sc_total)+" where nom='"+nom+"' and prenom='"+prenom+"'"
        c.execute(req_update)
    #Classement par rapport au score cumule
    req="select nom, prenom, score_cumule from etudiants"
    c.execute(req)
    tab_quiz=c.fetchall()
    tab_quiz.sort(key=lambda colonnes: colonnes[2])
    tab_quiz=np.flipud(tab_quiz)
    rank=1
    sc_quiz=[float(tab_quiz[0,2])]
    cl_quiz=[rank]
    for l in tab_quiz[1:]:
        #print(l[2],sc_quiz[-1])
        if float(l[2])==sc_quiz[-1]:
            cl_quiz.append(cl_quiz[-1])
            rank+=1
        else: 
            rank+=1
            cl_quiz.append(rank)
        sc_quiz.append(float(l[2]))
    tab_quiz=np.array(np.transpose(np.concatenate((np.mat(tab_quiz[:,0]),np.mat(tab_quiz[:,1]),np.mat(tab_quiz[:,2]),np.mat(np.array(cl_quiz))),axis=0)))
    tab_quiz2=[]
    for l in tab_quiz:
        c.execute("select classement from etudiants where nom='"+l[0]+"' and prenom='"+l[1]+"'")
        (classement_0,)=c.fetchone()
        # req_update="update etudiants set score_cumule="+str(sc_total)+" where nom='"+l[0]+"' and prenom='"+l[1]+"'"
        # c.execute(req_update)
        req_update="update etudiants set classement="+str(l[3])+" where nom='"+l[0]+"' and prenom='"+l[1]+"'"
        c.execute(req_update)
        req_update="update etudiants set evol_classement="+str(-int(l[3])+int(classement_0))+" where nom='"+l[0]+"' and prenom='"+l[1]+"'"
        c.execute(req_update)
        
conn.commit()
conn.close()



# #Post-traitement
# ###########@
conn=sqlite3.connect('mpsi_quizz.db')
c=conn.cursor()
# 
# #Generation du tableau html
# 
c.execute("select prenom, score_cumule, classement, evol_classement from etudiants")
data=c.fetchall()
data.sort(key=lambda colonnes: colonnes[2])
tableau=[]
for ligne in data:
    tableau.append(list(ligne))
texte='<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: center;"></thead>\n'
texte+='<th>Prénom</th>\n<th>Score</th>\n<th>Classement</th>\n<th>Evolution au classement</th>\n</tr>\n'
i=0
while i<=10:
    l=tableau[i]
    if l[3]>=0:
        texte+='<th>'+l[0]+'</th>\n<th>'+str(l[1])+'</th>\n<th>'+str(l[2])+'</th>\n<th>+'+str(l[3])+'</th>\n</tr>\n'
    else:
        texte+='<th>'+l[0]+'</th>\n<th>'+str(l[1])+'</th>\n<th>'+str(l[2])+'</th>\n<th>'+str(l[3])+'</th>\n</tr>\n'
    i+=1

texte+='</tbody>\n</table>'  
with open('tableau1.html','w',encoding='iso-8859-1') as f:
    f.write(texte)
#     
# texte='<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: center;"></thead>\n'
# texte+='<th>Nom</th>\n<th>Prénom</th>\n<th>Score</th>\n</tr>\n'
# i=21
# while i<=40:
#     l=tableau[i]
#     texte+='<th>'+l[0]+'</th>\n<th>'+l[1]+'</th>\n<th>'+str(l[2])+'</th>\n</tr>\n'
#     i+=1
# 
# texte+='</tbody>\n</table>'  
# with open('tableau2.html','w',encoding='iso-8859-1') as f:
#     f.write(texte)
# 
# 
#       
#                     

