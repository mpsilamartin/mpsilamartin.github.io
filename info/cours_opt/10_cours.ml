
(** Arbre binaire strict **)
type ('a, 'b) arbre =
  | Feuille of 'a
  | Noeud of 'b * ('a, 'b) arbre * ('a, 'b) arbre
;;

(* Exercice 2 *)
let arbre = Noeud ('*',
                   Noeud ('+',
                          Feuille 3,
                          Feuille 5),
                   Feuille 4
              )
;;
              
                        

(** Arbre binaire, éventuellement vide **)
type 'a arbre =
  | Nil
  | Noeud of 'a * 'a arbre * 'a arbre
;;

             
(** Nombre de noeuds, de feuilles **)
(* Exercice 3 *)
let rec nb_noeuds a =
  match a with
  | Nil -> 0
  | Noeud (_, fg, fd) ->
     1 + nb_noeuds fg + nb_noeuds fd
;;

let rec nb_feuilles a =
  match a with
  | Nil -> 0
  | Noeud (_, Nil, Nil) -> 1
  | Noeud (_, fg, fd) ->
     nb_feuilles fg + nb_feuilles fd
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
                
