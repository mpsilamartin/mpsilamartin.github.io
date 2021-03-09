(** Implémentation et fonctions élémentaires **)

type 'a arbre =
  | Vide
  | Noeud of 'a * 'a arbre * 'a arbre
;;

(* Q1 *)
let mon_arbre = Noeud (1,
                      Noeud (2,
                             Noeud (3, Vide, Vide),
                             Noeud (4, Vide, Vide)),
                      Noeud (5,
                             Noeud (6,
                                    Vide,
                                    Noeud (7, Vide, Vide)),
                             Noeud (8, Vide, Vide))
                 )
;;

(* Q2 *)
let rec est_strict a =
  match a with
  | Vide -> true
  | Noeud (_, Vide, Vide) -> true
  | Noeud (_, Vide, _) -> false
  | Noeud (_, _, Vide) -> false
  | Noeud (_, fg, fd) -> est_strict fg && est_strict fd
;;

est_strict mon_arbre;;

let mon_arbre_strict = Noeud (1,
                      Noeud (2,
                             Noeud (3, Vide, Vide),
                             Noeud (4, Vide, Vide)),
                      Noeud (5,
                             Noeud (6,
                                    Noeud (7, Vide, Vide),
                                    Noeud (8, Vide, Vide)),
                             Noeud (9, Vide, Vide))
                 )
;;

let un_arbre =
  Noeud (1,
         Noeud (2,
                Noeud (4,
                       Noeud (7,
                              Vide,
                              Vide),
                       Noeud(8,
                             Vide,
                             Vide)
                  ),
                Vide),
         Noeud (3,
                Noeud (10,
                       Vide, 
                       Vide),
                Noeud (6,
                       Noeud (9,
                              Vide,
                              Vide),
                       Noeud (5,
                              Vide,
                              Vide)
                  )
           )
    )
                
;;


est_strict mon_arbre_strict;;
est_strict un_arbre;;

(* Q3 *)
let rec nb_noeuds a =
  match a with
  | Vide -> 0
  | Noeud (_, fg, fd) -> 1 + nb_noeuds fg + nb_noeuds fd
;;

nb_noeuds mon_arbre;;


let rec nb_feuilles a =
  match a with
  | Vide -> 0
  | Noeud (_, Vide, Vide) -> 1
  | Noeud (_, fg, fd) -> nb_feuilles fg + nb_feuilles fd
;;

nb_feuilles mon_arbre;;

(* Q4 *)
let rec hauteur a =
  match a with
  | Vide -> -1
  (* ou 0 si on utilise l'autre définition de la hauteur *)
  | Noeud (_, fg, fd) -> 1 + max (hauteur fg) (hauteur fd)
;;

hauteur mon_arbre;;

(* Q5 *)
let rec recherche x a =
  match a with
  | Vide -> false
  | Noeud (e, fg, fd) -> x = e || recherche x fg || recherche x fd
;;

(** Quelques fonctions sur des arbres étiquetés par des entiers **)

(* Q6 *)

let rec maxi a =
  match a with
  | Vide -> failwith "Arbre vide"
  | Noeud (e, Vide, Vide) -> e
  | Noeud (e, fg, Vide) -> max e (maxi fg)
  | Noeud (e, Vide, fd) -> max e (maxi fd)
  | Noeud (e, fg, fd) -> max e (max (maxi fg) (maxi fd))
;;

maxi mon_arbre;;
maxi un_arbre;;

(* Q7 *)
let rec somme a =
  match a with
  | Vide -> 0
  | Noeud (e, fg, fd) -> e + somme fg + somme fd
;;

somme mon_arbre;;
somme un_arbre;;

(* Q8 *)
let rec somme_max_branche a =
  match a with
  | Vide -> 0
  | Noeud (e, fg, fd) -> e + max (somme_max_branche fg) (somme_max_branche fd)
;;

somme_max_branche mon_arbre;;

(** Diamètre d'un arbre **)
let rec diametre a =
  match a with
  | Vide -> 0
  | Noeud (_, fg, fd) ->
     let d_gauche = diametre fg and d_droit = diametre fd in
     let plc_par_racine = 2 + (hauteur fg) + (hauteur fd) in
     max plc_par_racine (max d_gauche d_droit)
;;

diametre mon_arbre;;

(** Peignes **)
type arbre =
  | Feuille of int
  | Noeud of arbre * arbre ;;

(* Q11 *)
let mon_peigne = Noeud (Noeud (Feuille 2,
                               Feuille 5),
                        Noeud (Feuille 1,
                               Noeud (Feuille 3,
                                      Feuille 4)

                          )
                   );;

let un_peigne = Noeud (Noeud (Feuille 1,
                               Noeud (Feuille 3,
                                      Feuille 4)

                          ),
                          Noeud (Feuille 2,
                                 Feuille 5)
                  )
;;

(* Q13 *)
let rec est_range a =
  match a with
  | Feuille _ -> true
  | Noeud (fg, Feuille _) -> est_range fg
  | _ -> false
;;

(* Q14 *)
let rec est_peigne_strict a =
  match a with
  | Feuille _ -> true
  | Noeud (Feuille _, fd) -> est_peigne_strict fd
  | Noeud (fg, Feuille _) -> est_peigne_strict fg
  | _ -> false
;;

let est_peigne a =
  match a with
  | Feuille _ -> true
  | Noeud (fg, fd) -> est_peigne_strict fg && est_peigne_strict fd
;;

(* Q15a *)
let peigne_rot = Noeud (Noeud (Noeud (Feuille 2,
                                      Feuille 5),
                               Feuille 1),
                        Noeud (Feuille 3,
                               Feuille 4)
                   );;
(* Q15b *)
let rotation a =
  match a with
  | Noeud (a1, v2) ->
     begin
       match v2 with
       | Feuille _ -> a
       | Noeud (a2, Feuille f) -> Noeud (Noeud (a1,
                                                Feuille f),
                                         a2)
       | Noeud (Feuille f, a2) -> Noeud (Noeud (a1,
                                                Feuille f),
                                         a2)
       | _ -> failwith "Cet arbre n'est pas un peigne"
     end
  | _ -> a
;;

rotation mon_peigne;;

(* Q15c *)
let rangement a =
  if not (est_peigne a)
  then a
  else
    let rec range peigne =
      match peigne with
      | Feuille _ -> peigne
      | Noeud (fg, Feuille f) -> Noeud (range fg, Feuille f)
      | _ -> range (rotation peigne)
    in
    range a
;;

rangement mon_peigne;;
