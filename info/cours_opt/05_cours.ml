(** Enregistrement avec champ modifiable **)
type etudiant = {
    nom : string;
    prenom : string;
    mutable classe : string;
  };;


let e = {
    nom = "Tournesol";
    prenom = "Tryphon";
    classe = "MPSI"
  };;

type 'a reference = {
    mutable contenu :'a
  };;

(** Références **)
let b = {contents = 2};;
b.contents;;
b.contents <- 3;;
b;;


let x = ref 0;; (* synonyme de let x = {contents = 0} *)
x := 3;; (* synonyme x <- 3;;*)
x := !x + 1;;
!x;;

incr x;;
!x;;

(** Types unit, fonctions avec effets de bord **)
let f () = print_string "Coucou";;

(** Séquences d'instructions **)
let classe nom numero =
  print_string ("Vivent les "^nom^" ");
  print_int numero;
  print_newline ();
  numero
;;

let est_pair n =
  if n mod 2 = 0
  then
    (print_endline "nombre pair";
     true;)
  else
    (print_endline "nombre impair";
     false;)
;;

let est_pair n =
  (if n mod 2 = 0
  then
    print_endline "nombre pair");
  true
;;
let est_pair n =
  if n mod 2 = 0
  then
    begin
      print_endline "nombre pair";
      true
    end
  else
    begin
      print_endline "nombre impair";
      false
    end
;;

(** Boucles **)
for i = 1 to 10
do
  print_int i;
  print_char ' '
done;;

for i = 10 downto 1
do
  print_int (2*i);
  print_char ' '
done;;

let a = ref 2020 in
    while !a > 0 do
      print_int (!a mod 2);
      a := !a / 2
    done
;;

(** Tableaux **)
let t1 = [|1; 2; 3; 4; 5; 6 |];;
Array.length t1;;
t1.(1);;
let t2 = Array.make 3 'a';;

t2.(1) <- "mpsi";;
t2.(1)<- 'm';;

let tabtab = Array.make 3 [|1|];;
tabtab.(0).(0)  <- 42;;


let tt = Array.make 4 (ref 5);;
