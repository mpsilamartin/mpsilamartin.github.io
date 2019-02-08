(** Type produit **)

(* Produit cartésien *)
type complexe = float*float;;

let partie_reelle z =
  match z with
  |(a, _) -> a

let module_complexe z =
  match z with
  |(a,b) -> sqrt(a**2. +. b**2.)
;;
let module_complexe (z:complexe) =
  match z with
  | (a,b) -> sqrt(a**2. +. b**2.)
;;

(* Enregistrements *)
type date = {
    jour : int;
    mois : int;
    annee : int;
  };;

let d = {annee = 2019; mois = 3; jour = 14;};;
          
let d = { mois = 3 ; jour = 14;}
      

type etudiant = {
    nom : string;
    prenom : string;
    naissance : date;
  }

let e = {
    nom = "Tournesol";
    prenom = "Tryphon";
    naissance = {
        jour = 28 ;
        mois = 1;
        annee = 2001;
      }
  };;

let est_majeur e =
  let n = e.naissance in
  let j = n.jour and m = n.mois
      and a = n.annee in
  let age = 2019 - a -
              (if m > 2 ||
                    (m = 2 && j > 5)
               then 1
               else 0) in
  age >= 18
;;

est_majeur e;;

(** Types sommes **)
(* Types énumérations *)
type jour_semaine =
  | Lundi
  | Mardi
  | Mercredi
  | Jeudi
  | Vendredi
  | Samedi
  | Dimanche
;;

let week_end j =
  match j with
  | Samedi -> true
  | Dimanche -> true
  | _ -> false
;;

type couleur =
  | Trefle
  | Carreau
  | Coeur
  | Pique
;;

type carte =
  | As of couleur
  | Roi of couleur
  | Dame of couleur
  | Valet of couleur
  | Petite_carte of int * couleur
;;

let valeur_carte atout = fun carte ->
  match carte with
  | As _ -> 11
  | Roi _ -> 4
  | Dame _ -> 3
  | Valet c -> if c = atout then 20 else 2
  | Petite_carte (10, _) -> 10
  | Petite_carte (9, c) -> if c = atout
                           then 14
                           else 0
  | _ -> 0
;;

type color =
  | Cyan
  | Magenta
  | Jaune
  | Melange of color * color
;;

let rouge = Melange (Magenta, Jaune);;
let orange = Melange (Melange (Jaune, Magenta), Jaune);;

let rec cmj coul =
  match coul with
  | Cyan -> 1., 0., 0.
  | Magenta -> 0., 1., 0.
  | Jaune -> 0., 0., 1.
  | Melange (co1, co2) ->
     let c1, m1, j1 = cmj co1
     and c2, m2, j2 = cmj co2
     in 0.5 *. (c1 +. c2), 0.5 *. (m1 +. m2),
        0.5 *. (j1 +. j2)
;;
