import sqlite3

conn = sqlite3.connect("mpsimdb.sqlite")
c = conn.cursor()

def ajoutpersonne(nom,prenom,datenaissance,curseur=c,connection=conn):
    """Ajoute la personne (nom,prenom,datenaissance) à la table PERSONNE"""
    req = """INSERT INTO PERSONNE(nom,prenom,datenaissance)
             VALUES(?,?,date(?));"""
    p = (nom,prenom,datenaissance)
    curseur.execute(req,p)
    connection.commit()
    return None

ajoutpersonne('HAMILL','Mark','1951-09-25')
