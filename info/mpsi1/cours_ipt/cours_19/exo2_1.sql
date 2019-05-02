SELECT * FROM PERSONNE
WHERE EXISTS (SELECT * FROM FILM
              WHERE PERSONNE.id = idrealisateur)
      AND
	  EXISTS (SELECT * FROM JOUE
              WHERE PERSONNE.id = idacteur);