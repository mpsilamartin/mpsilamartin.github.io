(* Exercice 1 *)
let rec binom1 n p =
  match (n, p) with
  | _, _ when n < p -> 0
  | _, _ when p < 0 -> 0
  | _, 0 -> 1
  | _, _ when p = n -> 1
  | _, _ -> (binom1 (n-1) p)
            + (binom1 (n-1) (p-1))
;;

let rec binom1bis n p =
  if n < p || p < 0
  then 0
  else
    if p = 0
    then 1
    else binom1bis (n-1) p
         + binom1bis (n-1) (p-1)
;;

let rec binom2 n p =
  if n < p || p < 0
  then 0
  else
    if p = 0
    then 1
    else n * binom2 (n-1) (p-1) / p
;;

(* Exercice 2 *)
let fact n =
  let rec aux n acc =
    match n with
    | 0 -> acc
    | _ -> aux (n-1) (n*acc)
  in
  aux n 1
;;

(* Exercice 3 *)
let rec pgcd a b =
  match b with
  | 0 -> a
  | _ -> pgcd b (a mod b)
;;

(* Exercice 4 *)
let rec pieces prix monnaie =
  match prix, monnaie with
  | 0, _ -> 1     
  | _, [] -> 0
  | _, t::q ->
     if prix < t
     then pieces prix q
     else pieces (prix-t) (t::q)
          + pieces prix q
;;
