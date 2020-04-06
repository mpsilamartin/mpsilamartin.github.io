(** Exercice 2 **)
let rec fact n acc =
  match n with
  | 0 -> acc
  | _ -> fact (n-1) (acc*n)
;;

fact 6 1;;

(** Exercice 3 **)
let rec pgcd a b =
  match b with
  | 0 -> a
  | _ -> pgcd b (a mod b)
;;

(* pgcd a b termine si b vaut 0 *)
(* si b est supérieur ou égal à 1, alors 1 seul appel récursif dont le 2ème argument est strictement inférieur à b*)

(** Exercice 4 **)
(* Écrire une fonction récursive prenant en argument une somme à atteindre, et une liste de valeurs de pièces/billets et qui renvoie le nombre de manières d'atteindre la somme *)

(* Cas de tests :
- 11 possibilités pour atteindre 10 avec 1,2,5,10
- 451 pour atteindre 50 avec 1, 2, 5, 10, 20, 50
 *)

let rec monnaie x liste =
  match liste with
  | [] -> 0
  | t::q -> if t = x
            then 1 + monnaie x q
            else
              if t < x
              then monnaie x q + monnaie (x-t) liste
              else monnaie x q
;;
