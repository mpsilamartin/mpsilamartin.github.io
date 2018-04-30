-- Acteurs ayant joué avec Martin Freeman
SELECT DISTINCT PERSONNE.nom,PERSONNE.prenom
FROM PERSONNE
JOIN JOUE ON PERSONNE.id = JOUE.idacteur
JOIN JOUE AS J2 ON JOUE.idfilm = J2.idfilm
JOIN PERSONNE AS P2 ON J2.idacteur = P2.id
WHERE P2.nom = 'Freeman';
