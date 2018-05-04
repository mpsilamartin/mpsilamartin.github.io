-- Nb d'acteurs qui ont joué au moins deux rôles
SELECT COUNT(*) AS nb_acteurs_plusieurs_rôles
FROM (SELECT COUNT(*) AS nb_roles
      FROM JOUE
      GROUP BY idacteur
      HAVING nb_roles >=2
     );
