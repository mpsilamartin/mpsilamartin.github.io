SELECT * 
FROM PERSONNE 
JOIN JOUE ON id = idacteur
JOIN (SELECT J2.idfilm AS n 
      FROM JOUE AS J2
	  JOIN PERSONNE AS P2 ON P2.id = J2.idacteur
	  WHERE P2.nom = 'Freeman')
	 ON JOUE.idfilm =  n;