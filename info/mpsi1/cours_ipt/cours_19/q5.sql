-- Acteurs ayant joué avec Martin Freeman
SELECT nom,prenom
FROM PERSONNE
JOIN JOUE ON idacteur = id
WHERE idfilm IN (SELECT FILM.id 
                 FROM FILM
                 JOIN JOUE ON FILM.id = idfilm
                 JOIN PERSONNE AS P2 ON idacteur = P2.id
                 WHERE P2.nom = 'Freeman'
		);
