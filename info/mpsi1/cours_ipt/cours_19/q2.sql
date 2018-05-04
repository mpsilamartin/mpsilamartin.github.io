-- Réalisateurs et acteurs à la fois
SELECT DISTINCT nom,prenom
FROM PERSONNE, FILM
WHERE EXISTS (SELECT idacteur
              FROM JOUE
              WHERE PERSONNE.id = idacteur
                    AND
                    idacteur = FILM.idrealisateur
             );
