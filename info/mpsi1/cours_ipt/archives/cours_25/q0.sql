.header ON

SELECT COUNT(*) AS nb_acteurs_plusieurs_rôles 
FROM (SELECT nom, prenom, COUNT(*) 
      FROM PERSONNE, JOUE
      WHERE PERSONNE.id=idacteur
      GROUP BY PERSONNE.id
      HAVING COUNT(*) >= 2
     );
