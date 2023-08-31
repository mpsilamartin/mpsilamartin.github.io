SELECT COUNT(DISTINCT nom) AS acteurs_nes_avant_1940
FROM PERSONNE
JOIN JOUE ON id = idacteur
WHERE datenaissance <= '1940-01-01';