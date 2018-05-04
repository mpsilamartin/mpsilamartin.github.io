-- Personne la plus jeune
SELECT nom, prenom, datenaissance
FROM PERSONNE, (SELECT MAX(P2.datenaissance) AS max_date
                              FROM PERSONNE AS P2
               )
WHERE datenaissance = max_date ;