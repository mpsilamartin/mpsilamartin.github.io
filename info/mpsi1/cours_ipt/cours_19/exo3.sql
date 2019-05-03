SELECT DISTINCT id, nom, prenom, datenaissance FROM PERSONNE
JOIN JOUE ON id = idacteur
WHERE datenaissance >= '1930-01-01';