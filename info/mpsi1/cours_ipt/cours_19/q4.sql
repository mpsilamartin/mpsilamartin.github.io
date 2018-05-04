-- Nb d'acteurs nés avant le 1er janvier 1940
SELECT COUNT(DISTINCT idacteur) AS nb_acteurs_nes_avant_1940
FROM PERSONNE
JOIN JOUE ON id = idacteur
WHERE datenaissance <= '1940-01-01';