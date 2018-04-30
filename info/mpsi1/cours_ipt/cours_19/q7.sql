-- Personne la plus jeune
SELECT nom, prenom, datenaissance
FROM PERSONNE
WHERE datenaissance = (SELECT MAX(P2.datenaissance)
                              FROM PERSONNE AS P2
                      );