import sqlite3

conn = sqlite3.connect("mpsimdb.sqlite")
c = conn.cursor()

c.execute("""SELECT * 
             FROM PERSONNE
             WHERE prenom = 'Clint'""")

def personnes(date_min,date_max,curseur=c):
    """Renvoie la liste des personnes nées entre date_min et date_max"""
    req = """SELECT nom, prenom
             FROM PERSONNE
             WHERE datenaissance >= ?
                   AND
                   datenaissance <= ? ;"""
    p = (date_min,date_max)
    curseur.execute(req,p)
    L = curseur.fetchall()
    return L
