(** Exercice 3 **)

(* Ecrire une fonction récursive qui calcule le pgcd de deux entiers naturels a et b*)
let rec pgcd a b =
  if a mod b = 0
  then if a < b
       then a
       else b
  else if a < b
  then pgcd a (b mod a)
  else pgcd b (a mod b)
;;

let rec pgcd a b =
  if b = 0
  then a
  else pgcd b (a mod b)
;;

(* Jutifier qu'elle termine *)
(* Si b = 0, la fonction termine,
Si b >= 1, alors l'appel récursif est réalisé avec un deuxième argument strictement plus petit que b*)


(** Exercice 4 **)
(* Ecrire une fonction récursive prenant en argument une somme à atteindre et une liste de valeurs de billets/pièces et qui renvoie le nombre de manière d'atteindre la somme *)

(* Cas de tests : 
- 11 possibilités pour 10 avec 1, 2, 5, 10
- 451 pour 50 avec 1, 2, 5, 10, 20, 50
 *)

let rec nb_possibilites somme liste =
  match liste with
  | [] -> if somme = 0
          then 1
          else 0
  | t::q -> if somme < t
            then nb_possibilites somme q
            else
              if somme = t
              then 1 + nb_possibilites somme q
              else nb_possibilites (somme-t) liste
                   + nb_possibilites somme q
;;
