(** Implémentation d'une file avec deux piles **)
type 'a file = {
    entree : 'a Stack.t;
    sortie : 'a Stack.t
  };;

(** Implémentation d'une file avec une liste circulaire **)
type 'a cellule = {valeur: 'a ; mutable suivant: 'a cellule};;
type 'a liste = Nil | Cellule of 'a cellule;;

type 'a file = {mutable queue : 'a liste};;

exception File_vide;;

(* Construction "à la main" de la file en exemple *)
let rec cellule7 = {
    valeur = 7 ;
    suivant = {
        valeur = 1 ;
        suivant = {
            valeur = 2 ;
            suivant = {
                valeur = 3 ;
                suivant = {
                    valeur = 4 ;
                    suivant = {
                        valeur = 5 ;
                        suivant = {
                            valeur = 6;
                            suivant = cellule7
                          }
                      }
                  }
              }
          }
      }
  }
;;

let ma_file = {queue = Cellule cellule7};;

(** Feu de forêt **)

(* Chargement du module graphique *)
#load "graphics.cma";;
open Graphics;;

Random.self_init ();;
(* Renvoie true avec une probabilité p, false avec une probabilité 1-p *)
let random_bool p =
  Random.float 1. < p
;;

(* Modifie la couleur du pixel de coordonnées (x,y) avec la couleur c*)
(* Exemples de valeur possibles pour c : red, blue, green, black *)
let couleur_point (x,y) c =
  set_color c ;
  plot (x) (y)
;;
  

let propagation p =
  (* Ouvre une fenêtre graphique de la taille spécifiée *)
  open_graph " 400x400" ;
  (* Crée une matrice - tableau de tableaux - de taille 400x400 dont tous les termes valent false *)
  let foret = Array.make_matrix 400 400 false in

  (* Algorithme à compléter *)
  ()
  
;;
      
