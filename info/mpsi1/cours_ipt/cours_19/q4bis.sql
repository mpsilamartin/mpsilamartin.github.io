-- Nb d'acteurs nés avant le 1er janvier 1940
SELECT COUNT(*) AS nb_acteurs_nes_avant_1940
FROM (SELECT DISTINCT idacteur 
      FROM PERSONNE
      JOIN JOUE ON id = idacteur
      WHERE datenaissance <= '1940-01-01'
     );
