(** Exercice 2 **)
(*  _::0::1::_ est un motif qui filtre les 
liste d'au moins 3 entiers dont 
le 2e est 0 et le 3e est 1 *)

(** Exercice 3 **)
let non_vide liste =
  not (liste = [])
;;

let non_vide liste =
  match liste with
  | [] -> false
  | _ -> true
;;

let exactement_deux_elts liste =
  match liste with
  | [_;_] -> true
  | _ -> false
;;
let exactement_deux_elts liste =
  match liste with
  | x::[y] -> true
  | _ -> false
;;
let exactement_deux_elts liste =
  match liste with
  | x::y::[] -> true
  | _ -> false
;;
let exactement_deux_elts liste =
  match liste with
  | [x;y] -> true
  | _ -> false
;;

let deux_ou_moins liste =
  match liste with
  | _::_::_::p -> false
  | _ -> true
;;

let premier_true liste =
  match liste with
  | true::_ -> true
  | _ -> false
;;

let premier_true liste =
  match liste with
  | [] -> false
  | t::_ -> t = true
;;

let prem_false_deux_true liste =
  match liste with
  | false::true::_ -> true
  | _ -> false
;;

let rec avant_dernier liste =
  match liste with
  | [] -> failwith "Liste vide"
  | [x] -> failwith "Un seul élément"
  | [x;y] -> x
  | t::q -> avant_dernier q
;;

let rec avant_dernier liste =
  match liste with
  | x::y::q -> if q = []
               then x
               else avant_dernier (y::q)
  | _ -> failwith "Pas bien !"
;;

(** Exercice 4 **)
let rec carres liste =
  match liste with
  | [] -> []
  | t::q -> (t*t)::carres q
;;

(** Exercice 5 **)
let rec somme liste =
  match liste with
  | [] -> 0
  | t::q -> t + somme q
;;

(** Exercice 6 **)
(* Renvoie la longueur de la liste *)
let rec length liste =
  match liste with
  | [] -> 0
  | _::q -> 1 + length q
;;

(* Renvoie un booléen indiquant si e est dans liste *)
let rec mem e liste =
  match liste with
  | [] -> false
  | t::q -> if t = e
            then true
            else mem e q
;;

let rec mem e liste =
  match liste with
  | [] -> false
  | t::q -> t = e || mem e q
;;

let rec map f liste =
  match liste with
  | [] -> []
  | t::q -> (f t)::(map f q)
;;
