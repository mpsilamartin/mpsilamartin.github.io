-- Liste des réalisateurs ayant dirigé Eastwood

SELECT REALISATEUR.nom, REALISATEUR.prenom
FROM PERSONNE AS REALISATEUR
JOIN FILM ON idrealisateur = REALISATEUR.id
JOIN JOUE ON idfilm = FILM.id
JOIN PERSONNE AS ACTEUR ON idacteur = ACTEUR.id
WHERE ACTEUR.nom = 'Eastwood';