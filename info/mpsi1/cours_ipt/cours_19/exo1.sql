SELECT COUNT(*) AS nb_acteurs_plusieurs_roles
FROM (SELECT COUNT(*) as nb_roles
      FROM PERSONNE
	  JOIN JOUE ON PERSONNE.id = idacteur
	  GROUP BY PERSONNE.id
	  HAVING nb_roles >= 2);