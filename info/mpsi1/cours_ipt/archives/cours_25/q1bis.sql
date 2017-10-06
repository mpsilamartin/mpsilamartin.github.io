.header ON

SELECT DISTINCT nom, prenom
FROM PERSONNE, JOUE, FILM
WHERE PERSONNE.id = idacteur
      AND
      PERSONNE.id = idrealisateur;
