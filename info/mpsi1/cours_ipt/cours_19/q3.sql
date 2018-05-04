-- Acteurs nés après le 1er janvier 1930
SELECT DISTINCT nom,prenom,datenaissance
FROM PERSONNE
JOIN JOUE ON idacteur = PERSONNE.id
WHERE datenaissance >= '1930-01-01';