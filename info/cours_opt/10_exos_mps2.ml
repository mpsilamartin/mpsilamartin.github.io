(* Exercice 7 *)

let rec recherche_max arbre =
  match arbre with
  | Nil -> min_int
  | Noeud (x, fg, fd) ->
     max (max (recherche_max fg) x) (recherche_max fd)
;;

let rec maxi arbre =
  match arbre with
  | Nil -> failwith "Arbre vide"
  | Noeud (x, Nil, Nil) ->
     x
  | Noeud (x, fg, Nil) ->
     max x (maxi fg)
  | Noeud (x, Nil, fd) ->
     max x (maxi fd)
  | Noeud (x, fg, fd) ->
     max (max x (maxi fg)) (maxi fd)
;;
       
let rec somme_max a =
  match a with
  | Nil -> 0
  | Noeud (x, fg, fd) ->
     x + max (somme_max fg) (somme_max fd)
;;

(* Exercice 8 *)

let arbre_binaire_complet h =
  let rec aux h rac =
    match h with
    | 0 -> Noeud(rac, Nil, Nil)
    | _ -> Noeud(rac,
                  aux (h-1) (rac*2),
                  aux (h-1) (2*rac +1)
             )
  in
  aux h 1
;;

let numeroter a =
  let rec aux tree n_root =
    match tree with
    | Nil -> Nil
    | Noeud (x, fg, fd) ->
       Noeud ( (x, n_root),
               aux fg (2*n_root),
               aux fd (2*n_root + 1)
         )
;;

    
