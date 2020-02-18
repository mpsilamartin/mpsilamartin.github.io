(** Listes **)

(* Première implémentation *)

type 'a liste =
  | Nil
  | Cons of 'a * ('a liste)
;;

let lst = Cons (4, Cons (1, Cons (3, Nil)));;

let est_vide l =
  match l with
  | Nil -> true
  | _ -> false
;;

let tete l =
  match l with
  | Cons (t, _) -> t
  | _ -> failwith "Liste vide"
;;

let queue l =
  match l with
  | Cons (_, q) -> q
  | _ -> failwith "Liste vide"
;;

(* Implémentation OCaml *)
let est_vide l =
  match l with
  | [] -> true
  | _ -> false
;;

let tete l =
  match l with
  | [] -> failwith "Liste vide"
  | t::q -> t
;;

let queue l =
  match l with
  | [] -> failwith "Liste vide"
  | t::q -> q
;;

