SELECT DISTINCT PERSONNE.id, nom, prenom, datenaissance
FROM FILM
JOIN PERSONNE ON PERSONNE.id = idrealisateur
JOIN JOUE ON PERSONNE.id = idacteur;