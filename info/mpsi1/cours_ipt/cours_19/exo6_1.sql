SELECT DISTINCT PERSONNE.*
FROM PERSONNE -- table des réalisateurs
JOIN FILM ON PERSONNE.id = idrealisateur
JOIN JOUE ON FILM.id = idfilm
JOIN PERSONNE AS P2 ON P2.id = idacteur -- table des acteurs
WHERE P2.nom = 'Eastwood';