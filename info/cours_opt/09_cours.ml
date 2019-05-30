(* Liste d'associations *)
type ('a, 'b) entree =
  {cle : 'a ; valeur : 'b};;
type ('a, 'b) table =
  {mutable contenu : ('a, 'b) entree list};;


let creer_table () =
  {contenu = []}
;;

let ajouter tbl c v =
  let rec aux l =
    match l with
    | [] -> [{cle = c ; valeur = v}]
    | t::q -> if t.cle = c
              then {cle = c; valeur = v}::q
              else t::(aux q)
  in tbl.contenu <- aux tbl.contenu
;;

let supprimer tbl c =
  let rec aux l =
    match l with
    | [] -> []
    | t::q -> if t.cle = c
              then q
              else t::(aux q)
  in tbl.contenu <- aux tbl.contenu
;;
  
exception NonTrouve
let trouver tbl c =
  let rec aux l =
    match l with
    | [] -> raise NonTrouve
    | t::q -> if t.cle = c
              then t.valeur
              else aux q
  in aux tbl.contenu
;;

let ma_table = creer_table () ;;

ajouter ma_table "chocolat" 42;;
ma_table;;

ajouter ma_table "pomme" 9;;
ajouter ma_table "poire" 1515;;
ajouter ma_table "pomme" 1789;;

trouver ma_table "chocolat";;

supprimer ma_table "poire";;

ma_table;;

(* Table de hachage *)
type ('a, 'b) table = {
    h : 'a -> int ;
    contenu : ('a, 'b) entree list array
  };;

let creer_table m =
  { h = (function x -> x mod m) ; contenu = Array.make m [] }
;;

let ajouter tbl c v =
  let i = tbl.h c in
  let rec aux l =
    match l with
    | [] -> [{cle = c ; valeur = v}]
    | t::q -> if t.cle = c
              then {cle = c ; valeur = v}::q
              else t::(aux q)
  in tbl.contenu.(i) <- aux tbl.contenu.(i)
;;

let supprimer tbl c =
  let i = tbl.h c in
  let rec aux l =
    match l with
    | [] -> []
    | t::q -> if t.cle = c
              then q
              else t::(aux q)
  in tbl.contenu.(i) <- aux tbl.contenu.(i)
;;

let trouver tbl c =
  let i = tbl.h c in
  let rec aux l =
    match l with
    | [] -> raise NonTrouve
    | t::q -> if t.cle = c
              then t.valeur
              else (aux q)
  in aux tbl.contenu.(i)
;;

let code s =
  let n = String.length s in
  let somme = ref 0 in
  for i = 0 to n-1 do
    somme := !somme + Char.code s.[i]
  done;
  !somme
;;


let ma_table = creer_table 911 ;;

ajouter ma_table (code "chocolat") 42;;
ma_table;;

ajouter ma_table (code "pomme") 9;;
ajouter ma_table (code "poire") 1515;;
ajouter ma_table (code "pomme") 1789;;

trouver ma_table (code "chocolat");;

supprimer ma_table (code "poire");;

trouver ma_table (code "poire");;

(* Module Hashtbl *)

let ma_table = Hashtbl.create 10;;
Hashtbl.add ma_table "chocolat" 42;;
Hashtbl.add ma_table "pomme" 9;;
Hashtbl.add ma_table "poire" 1515;;

Hashtbl.stats ma_table;;

Hashtbl.find ma_table "chocolat";;
Hashtbl.find ma_table "poire";;
Hashtbl.find ma_table "pomme";;

Hashtbl.add ma_table "pomme" 1789;;

Hashtbl.stats ma_table;;

Hashtbl.remove ma_table "poire";;
Hashtbl.find ma_table "poire";;

Hashtbl.remove ma_table "pomme";;
Hashtbl.find ma_table "pomme";;

let ma_table = Hashtbl.create 10;;
Hashtbl.add ma_table "abricot" 27;;
Hashtbl.add ma_table "kiwi" 4;;
Hashtbl.stats ma_table;;
