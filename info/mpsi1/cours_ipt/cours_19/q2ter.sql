-- Réalisateurs et acteurs à la fois
SELECT DISTINCT nom,prenom
FROM PERSONNE
JOIN FILM ON PERSONNE.id = idrealisateur
JOIN JOUE ON PERSONNE.id = idacteur;