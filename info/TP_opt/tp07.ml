(* Q1 *)
let hash_int m k =
  k mod m
;;

  (* Q2 *)
let int_of_string_rec str =
  let n = String.length str in
  let rec aux i somme =
    if i = 0
    then somme
    else
      aux (i-1)
	  (int_of_char (String.get str (i-1))
	   + 256*somme)
  in aux n 0
;;
    
let int_of_string str =
  let n = String.length str in
  let somme = ref 0 in
  for i = n-1 downto 0 do
    somme := 256 * !somme
	     + int_of_char (String.get str i)
  done;
  !somme
;;
  (* Q3 *)
let hash_string m caract =
  let fromage = int_of_string caract in
  hash_int m fromage
;;

  (* Q4 *)

type ('a, 'b) table = {
  h : 'a -> int ;
  contenu : ('a* 'b) list array
}
;;

let creer_table funh w =
  {
    h = funh ;
    contenu = Array.make w []
  }
;;

  (* Q5 *)

let rec appartient lst cle =
  match lst with
  | [] -> false
  | (c,v)::q -> if c = cle
		then true
		else appartient q cle
;;

let contient tbl cle =
  (* On calcule l'indice où se trouverait la clé *)
  let i = tbl.h cle in
  appartient tbl.contenu.(i) cle
;;

(* Q6 *)
  
let trouver tbl cle =
  let i = tbl.h cle in
  let rec cherche lst cle =
     match lst with
     | [] -> raise Not_found
     | (c,v)::q -> if c = cle
		   then v
		   else appartient q cle
  in
  cherche tbl.contenu.(i) cle
;;
				   
  (* Q7 *)
(* On écrase l'ancienne valeur si la clé
est déjà dans la table *)
let rec ajout_liste lst cle valeur =
  match lst with
  | [] -> [(cle, valeur)]
  | (c, v)::q ->
     if c = cle
     then (cle, valeur)::q
     else (c,v)::(ajout_liste q cle valeur)
;;

let ajouter tbl cle valeur =
  let i = tbl.h cle in
  let new_liste_i =
    ajout_liste tbl.contenu.(i) cle valeur
  in
  tbl.contenu.(i) <- new_liste_i
;;
  
