SELECT COUNT(DISTINCT id)
FROM PERSONNE
JOIN JOUE AS J1 ON id = J1.idacteur
JOIN JOUE AS J2 ON id = J2.idacteur
WHERE J1.idfilm != J2.idfilm
      OR 
	  J1.idpersonnage != J2.idpersonnage;
