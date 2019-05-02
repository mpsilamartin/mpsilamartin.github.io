SELECT DISTINCT PERSONNE.*
FROM PERSONNE -- table des réalisateurs
JOIN FILM ON PERSONNE.id = idrealisateur
JOIN JOUE ON FILM.id = idfilm
WHERE idacteur = (SELECT id
                  FROM PERSONNE AS P2
				  WHERE P2.nom = 'Eastwood');