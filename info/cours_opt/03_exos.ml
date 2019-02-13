(* Exercice 3 *)
let non_vide = fun lst ->
  not (lst = [])
;;

let non_vide = fun lst ->
  lst <> []
;;
let non_vide l =
  match l with
  | [] -> false
  | _ -> true
;;

let liste_deux_elts = fun x ->
  match x with
  | [_;_] -> true
  | _ -> false
;;

let liste_deux_elts = fun x ->
  match x with
  | _::_::[] -> true
  | _ -> false
;;

let liste_deux_ou_moins liste =
  match liste with
  | x::y::z::_ -> false
  | _ -> true
;;

let liste_deux_ou_moins liste =
  match liste with
  | _::_::_::_ -> false
  | _ -> true
;;

let liste_premier_true x =
  match x with
  | true::_ -> true
  | _ -> false
;;


let liste_false_true_truc l =
  match l with
  | false::q -> liste_premier_true q
  | _ -> false  
;;

let liste_false_true_truc l =
  match l with
  | false::true::_ -> true
  | _ -> false
;;
let liste_false_true_truc l =
  match l with
  | false::z::_ -> z
  | _ -> false
;;

let rec avant_dernier l =
  match l with
  | [] -> failwith "Liste vide"
  | [_] -> failwith "Un seul élément"
  | [x; y] -> x
  | t::q -> avant_dernier q
;;
let rec avant_dernier l =
  match l with
  | [] -> failwith "Pas assez d'éléments"
  | [x; y] -> x
  | t::q -> avant_dernier q
;;

(* Exercice 4 *)
let rec carre l =
  match l with
  | [] -> []
  | t::q -> (t*t) :: (carre q)
;;

let rec carre_float l =
  match l with
  | [] -> []
  | t::q -> (t**2.) :: (carre_float q)
;;

(* Exercice 5 *)
let rec somme l =
  match l with
  | [] -> 0
  | t::q -> t + (somme q)
;;

(* Exercice 6 *)
let rec length l =
  match l with
  | [] -> 0
  | t::q -> 1 + (length q)
;;
(* Complexité : si n est le nombre d'éléments de la liste, on effectue n+1 appels récursifs chacun en O(1), donc fonction en O(n) *)

let rec mem x l =
  match l with
  | [] -> false
  | t::q -> t = x || mem x q
;;
    

let rec mem x l =
  match l with
  | [] -> false
  | t::q -> if t = x
            then true
            else mem x q
;;
    
(* Complexité pire cas : linéaire *)

let rec map f l =
  match l with
  | [] -> []
  | t::q -> (f t)::(map f q)
;;
(* Complexité linéaire *)

let rec filter f l =
  match l with
  | [] -> []
  | t::q -> if f t
            then t::(filter f q)
            else filter f q
;;
(* Complexité linéaire *)

  
let rec filter f l =
  match map f l with
  | [] -> []
  | false::_ -> filter f (List.tl l)
  | _ -> (List.hd l)::(filter f (List.tl l))
;;
(* Complexité quadratique !!! *)

(* Juste pour s'amuser *)
let filter f l =
  let rec aux l1 l2 =
    match (l1, l2) with
    | t1::q1, true::q2 -> t1::(aux q1 q2)
    | t1::q1, _::q2 -> aux q1 q2
    | _ -> []
  in
  aux l (map f l)
;;
  
(* en décomposant *)
let rec aux l1 l2 =
  match (l1, l2) with
  | t1::q1, true::q2 -> t1::(aux q1 q2)
  | t1::q1, _::q2 -> aux q1 q2
  | _ -> []
;;

let filter f l =
  aux l (map f l)
;;

(* Exercice 7 *)

let rec liste n =
  match n with
  | 0 -> []
  | n -> 1::(map (fun x -> x+1) (liste (n-1)))  
;;
(* Complexité quadratique : pas terrible... *)

let enum n =
  (* constr n k construit [k; ...; n] *)
  let rec constr n k =
    match n-k with
    | 0 -> n::[]
    | _ -> k::constr n (k+1)
  in
  constr n 1
;;
(* A reprendre pour la liste vide *)

let enum n =
  (* constr n deb construit une liste de n entiers successifs à partir de deb*)
  let rec constr n deb =
    match n with
    | 0 -> []
    | _ -> deb::(constr (n-1) (deb + 1))
  in
  constr n 1
;;

(* Exercice 8 *)

let rec append l1 l2 =
  match l1 with
  | [] -> l2
  | t::q -> t::(append q l2)
;;
(* Linéaire par rapport à la longueur de l1 *)
