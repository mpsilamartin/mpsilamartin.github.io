(** Exercice 2 **)
(*  _::0::1::_ est un motif qui filtre les 
liste d'au moins 3 entiers dont 
le 2e est 0 et le 3e est 1 *)

(** Exercice 3 **)
let non_vide l =
  match l with
  | [] -> false
  | _ -> true
;;

let non_vide l =
  not (l = [])
;;

let exact_deux_elts liste =
  match liste with
  | [_; _] -> true
  | _ -> false
;;

let au_plus_deux_elts liste =
  match liste with
  | [] -> true
  | [_] -> true
  | [_; _] -> true
  | _ -> false
;;
let au_plus_deux_elts liste =
  match liste with
  | a::b::c::q -> false
  | _ -> true
;;

let au_plus_deux_elts liste =
  match liste with
  | _::_::_::_ -> false
  | _ -> true
;;

let prem_true liste =
  match liste with
  | a::_ -> a = true
  | _ -> false
;;

let prem_true liste =
  match liste with
  | a::_ -> a
  | _ -> false
;;

let prem_true liste =
  match liste with
  | true::_ -> true
  | _ -> false
;;

let prem_false_deux_true liste =
  match liste with
  |false::true::_ -> true
  | _ -> false
;;

let prem_false_deux_true liste =
  match liste with
  | a::b::_ -> (not a) && b
  | _ -> false
;;

let rec avant_dernier liste =
  match liste with
  | [a; b] -> a
  | [_] -> failwith "Trop court"
  | [] -> failwith "Vide"
  | t::q -> avant_dernier q
;;

(** Exercice 4 **)

let rec liste_au_carre liste =
  match liste with
  | [] -> []
  | t::q -> t*t::liste_au_carre q
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
  | t::q -> f t :: map f q
  | [] -> []
;;

let rec filter f l =
  match l with
  | [] -> []
  | t::q -> if f t
            then t::filter f q
            else filter f q
;;

(** Exercice 7 **)
let rec mauvais_ordre n =
  match n with
  | 0 -> []
  | _ -> n::mauvais_ordre (n-1)
;;

let bon_ordre n =
  let rec complete l =
    match l with
    | h::t -> if h = 1
              then l
              else complete ((h-1)::l)
  in
  match n with
  | 0 -> []
  | _ -> complete [n]
;;

let bon_ordre n =
  let rec range p =
    match p with
    | 0 -> []
    | x -> (n - x + 1)::(range (x-1))
  in
  range n
;;

let bon_ordre n =
  let rec commence_par deb p =
    match p with
    | 0 -> []
    | _ ->
       deb::commence_par (deb+1) (p-1)
  in
  commence_par 1 n
;;

(** Exercice 8 **)
let rec append l n =
  match l with
  | [] -> n
  | t::q -> t::append q n
;;
(* Complexité : linéaire en la 
longueur de la 1ère liste *)

let append l n =
  l@n
;;

(** Exercice 9 **)

(* Renvoie les deux min (a,b) 
avec a <= b *)
let rec min l =
  match l with
  | [a; b] -> if a < b
              then (a, b)
              else (b, a)
  | x::y -> let (a, b) = min y
            in
            if x < a
            then (x, a)
            else
              if x < b
              then (a, x)
              else (a, b)
;;


