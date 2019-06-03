type 'a arbre =
  | Nil
  | Noeud of 'a * 'a arbre * 'a arbre
;;

let mon_arbre =
  Noeud (1,
         Noeud (2,
                Noeud (4,
                       Noeud (7,
                              Nil,
                              Nil),
                       Noeud(8,
                             Nil,
                             Nil)
                  ),
                Nil),
         Noeud (3,
                Noeud (5,
                       Nil, 
                       Nil),
                Noeud (6,
                       Noeud (9,
                              Nil,
                              Nil),
                       Noeud (10,
                              Nil,
                              Nil)
                  )
           )
    )
;;

(* Exercice 7 *)
let rec mouton a =
  match a with
  | Nil -> failwith "Arbre vide"
  | Noeud (e, Nil, Nil) -> e
  | Noeud (e, fg, Nil) ->
     max (mouton fg)  e
  | Noeud (e, Nil, fd) ->
     max  (mouton fd) e
  | Noeud (e, fg, fd) ->
     max (max (mouton fg) (mouton fd)) e
;;
      
