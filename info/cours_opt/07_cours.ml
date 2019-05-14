(** Piles **)
(* Implémentation avec une liste *)
type 'a pile = {
    mutable contenu : 'a list
  };;

let creer_pile () =  {contenu = []};;

let est_vide p = p.contenu = [] ;;

let empile x p =
  p.contenu <- x::p.contenu
;;

exception PileVide;;
let depile p =
  match p.contenu with
  | [] -> raise PileVide
  | t::q -> p.contenu <- q ; t
;;


(* Implémentation avec un tableau *)
exception PileVide;;
            
type 'a pile = {
    mutable hauteur : int ;
    pile : 'a array
  }
;;


let creer_pile n i =  {
    hauteur = 0 ;
    pile = Array.make n i
  }
;;

let est_vide p = p.hauteur = 0
;;

exception PilePleine;;
let empile x p =
  if p.hauteur = Array.length p.pile 
  then raise PilePleine
  else
    begin
      p.pile.(p.hauteur) <- x ;
      p.hauteur <- p.hauteur + 1 
    end
;;

exception PileVide;;
let depile p =
  if p.hauteur = 0
  then raise PileVide 
  else
    begin
      p.hauteur <- p.hauteur - 1 ;
      p.pile.(p.hauteur)
    end
;;

(* Module Stack *)
let maPile = Stack.create();;

Stack.push 0 maPile;;

maPile;;

for i = 1 to 6 do
  Stack.push i maPile
done;;

while not (Stack.is_empty maPile) do
  print_int (Stack.pop maPile);
  print_char ' '
done;;

(** Files **)
(* Avec deux listes *)
type 'a file = {
    mutable entree : 'a list ;
    mutable sortie : 'a list
  };;

let creer_file () = {entree = []; sortie = []};;

let est_vide f = f.entree = [] && f.sortie = [];;

let enfile f x =  f.entree <- x::f.entree;;

let miroir lst =
  let rec aux lst acc =
    match lst with
    | [] -> acc
    | t::q -> aux q (t::acc)
  in
  aux lst [];;

exception FileVide;;

let defile f =
  if f.sortie = []
  then
    while not (f.entree = []) do
      match f.entree with
      | t::q -> f.sortie <- t::f.sortie;
                f.entree <- q
    done;
  match f.sortie with
  | [] -> raise FileVide
  | t::q -> f.sortie <- q;
            t
;;

let rec defile f =
  match f.sortie with
  | t::q -> f.sortie <- q ; t
  | [] ->
     match f.entree with
     | [] -> raise FileVide
     | _ -> f.sortie <- miroir f.entree ;
            f.entree <- [] ;
            defile f
;;


(* Avec un tableau *)

type 'a file =  {
    mutable longueur : int ;
    mutable debut : int ;
    mutable fin : int ;
    file : 'a array };;

let creer_file n i =  {
    longueur = 0 ;
    debut = 0;
    fin = 0 ;
    file = Array.make n i
  };;

let est_vide f = f.longueur = 0 ;;

exception FilePleine
let enfile x f = 
  let n = Array.length f.file in
  if f.longueur = n
  then raise FilePleine
  else
    begin
      f.file.(f.fin) <- x ;
      f.fin <- (f.fin + 1) mod n ;
      f.longueur <- f.longueur + 1
    end
;;

exception FileVide
let defile f =
  let n = Array.length f.file in
  if est_vide f
  then raise FileVide
  else
    begin
      let x = f.file.(f.debut) in
      f.debut <- (f.debut + 1) mod n ;
      f.longueur <- f.longueur - 1;
      x 
    end
;;

(* Module Queue *)
let maFile = Queue.create ();;

for i = 1 to 15 do
  Queue.add i maFile
done;;

while not (Queue.is_empty maFile) do
  print_int (Queue.take maFile);
  print_char ' '
done;;
