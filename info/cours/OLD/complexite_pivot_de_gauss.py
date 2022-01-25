#Hypothèse : Les affections sont à coûts constant

#resout comporte 3 affectations et un appel aux fonctions descente et remontee

#descente comporte une affectations et une boucle  de (n-1) itérations.

# dans chaque itération on fait un appel à echange_lignes, cherche pivot et dans laquel on fait une boucle de (n-1) itérations dans le pire des cas qui comprend une affectation et pour chaque colonne de A (qui contient n colonnes) : 1 affectation une multiplication par une variable et une addition.

#On a un nombre d'opération de l'ordre de n**3. On a une complexité en o(n**3)

#Complextité de echange_lignes : en o(n) car pour chaque colonne de A on fait une double affectations

#Cherche pivot : dans le pire des cas (n-1) opérations et dans chacune d'elle, un nombre fini d'itération.

#On obtient donc une complexité cubique.

#Pour la phase de remontée : décompte du nombre d'opérations :
#somme(i=1->n)[1(division)+1(multiplication)+(n-i)(soustration+multiplication)]
#=2*n+2*[(1+n-1)*(n-1)/2]<C*n**2=>o(n**2)


#Complexité de contruction_successeurs du DS :
#On a 2 affections, 1 appel à la fonction moyenne et une boucle avec (n-1) itération.
#Dans le programme proposé en correction, dans chaque itération, on fait une comparation avec un appel avec la fonction ind_premier_pzd, et on fait 1 concaténation dans le pire des cas. Sans tenir compte de ind_premier_pzd (on doit stocker dans une variable le résultat de ind_premier_pzd) on a une complexité linaire



