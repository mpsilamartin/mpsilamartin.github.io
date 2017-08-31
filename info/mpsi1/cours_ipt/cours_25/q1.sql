.header ON

SELECT nom, prenom 
FROM PERSONNE 
WHERE EXISTS (SELECT * 
              FROM JOUE 
              WHERE PERSONNE.id = idacteur
             )
      AND
      EXISTS (SELECT * 
              FROM FILM 
              WHERE PERSONNE.id = idrealisateur
             );
