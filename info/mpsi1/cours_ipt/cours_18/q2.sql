-- Pour chaque film, liste des personnages

SELECT titre, PERSONNAGE.nom
FROM  JOUE
JOIN PERSONNAGE ON PERSONNAGE.id = idpersonnage 
JOIN FILM ON FILM.id = idfilm;