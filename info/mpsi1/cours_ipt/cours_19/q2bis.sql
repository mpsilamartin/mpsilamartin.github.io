-- Réalisateurs et acteurs à la fois
SELECT DISTINCT nom, prenom
FROM PERSONNE, FILM, JOUE
WHERE PERSONNE.id = idrealisateur
      AND
      PERSONNE.id = idacteur;
