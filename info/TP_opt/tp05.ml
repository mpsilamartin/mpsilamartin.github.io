(** Implémentation d'une file avec une liste circulaire **)
type 'a cellule = {valeur: 'a ; mutable suivant: 'a cellule};;
type 'a liste = Nil | Cellule of 'a cellule;;

type 'a file = {mutable queue : 'a liste};;

exception File_vide;;

let creer_file () =
  {queue = Nil}
;;

let defiler f =
  match f.queue with
  | Nil -> raise File_vide
  | Cellule c -> let tete = c.suivant in
                 if tete == c
                 then f.queue <- Nil
                 else c.suivant <- tete.suivant;
                 tete.valeur
;;

let enfiler x f =
  match f.queue with
  | Nil -> let rec new_cell = {valeur = x ; suivant = new_cell} in
           f.queue <- Cellule new_cell      
  | Cellule c -> let tete = c.suivant in
                 let new_cell = {valeur = x; suivant = tete} in
                 c.suivant <- new_cell;
                 f.queue <- Cellule new_cell
;;

let ma_file = creer_file ();;

for i = 1 to 5 do
  enfiler i ma_file
done;;

for i = 1 to 3 do
    print_int (defiler ma_file);
    print_char ' '
done;;

enfiler 6 ma_file;;
enfiler 7 ma_file;;
  

try
  while true do
    print_int (defiler ma_file);
    print_char ' '
  done
with
| File_vide -> ()
;;

(** Implémentation d'une file avec deux piles **)
type 'a file = {
    entree : 'a Stack.t;
    sortie : 'a Stack.t
  };;

let creer_file () =
  {entree = Stack.create ();
   sortie = Stack.create ()
  }
;;

let enfiler x f =
  Stack.push x f.entree
;;

let defiler f =
  if Stack.is_empty f.sortie
  then
    if Stack.is_empty f.entree
    then raise File_vide
    else
      while not (Stack.is_empty f.entree) do
        Stack.push (Stack.pop f.entree) f.sortie
      done;
  Stack.pop f.sortie
;;


let ma_file = creer_file ();;

for i = 1 to 5 do
  enfiler i ma_file
done;;

for i = 1 to 3 do
    print_int (defiler ma_file);
    print_char ' '
done;;

enfiler 6 ma_file;;
enfiler 7 ma_file;;
  

try
  while true do
    print_int (defiler ma_file);
    print_char ' '
  done
with
| File_vide -> ()
;;

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
  (* Crée une matrice de taille 400x400 dont tous les termes valent false *)
  let foret = Array.make_matrix 400 400 false in
  let file = creer_file () in
  
  let allume (x,y) c =    foret.(x).(y) <- true ;
    enfiler (x,y) file;
    couleur_point (x,y) red
  in
  allume (200,200) red;
  (*allume (100,100) red ;*)
  let traite (x,y) c =
(*if point_color x y = white then*)    
    if x >= 0 && x < 400 
      && y >= 0 && y < 400 && not foret.(x).(y) then

      if random_bool p then
	allume (x,y) c
  in
  try
    while true do
      let (x,y) = defiler file in
      (* let c = point_color x y in *)
      traite (x-1,y) red ;
      traite (x,y-1) red ;
      traite (x+1,y) red ;
      traite (x,y+1) red
    done; 
    print_string "Appuyer sur une touche pour fermer le dessin" ;
    close_graph ()
  with
    | File_vide-> ignore (read_key ()) ; close_graph ()
;;
      
propagation 0.5 ;;
