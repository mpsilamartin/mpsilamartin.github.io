(* Exercice 1 *)
let bissextile annee =
  if annee mod 100 = 0
  then annee mod 400 = 0
  else annee mod 4 =0
;;

let bissextile annee =
  if annee mod 4 = 0
  then if annee mod 100 = 0
       then annee mod 400 = 0
       else false
  else false
;;

let nb_jours m a =
  match m with
  | 2 -> if bissextile a then 29 else 28
  | 4 -> 30
  | 6 -> 30
  | 9 -> 30
  | 11 -> 30
  | _ -> 31
;;

let date_valide j m a =
  let nb_j = nb_jours m a in
  m >= 0 && m <= 12 && j >= 0 && j <= nb_j
;;

let nom_jour n =
  match n with
  | 0 -> "dimanche"
  | 1 -> "lundi"
  | 2 -> "mardi"
  | 3 -> "mercredi"
  | 4 -> "jeudi"
  | 5 -> "vendredi"
  | 6 -> "samedi"
;;
  
let zeller j m a =
  let p = if  m <= 2 then m+10 else m-2 in
  let b = if  m <= 2 then a-1 else a in
  let c = b / 100 in
  let d = b - 100*c in
  let n = j
	  + int_of_float (2.6 *. float_of_int p -. 0.2)
	  + d
	  + int_of_float (float_of_int d /. 4.)
	  + int_of_float (float_of_int c /. 4.)
	  + 5*c
  in n mod 7
;;

let jour_semaine j m a =
  if date_valide j m a
  then nom_jour (zeller j m a)
  else failwith "date invalide"
;;	   