(** Exercice 1 **)
let x = ref 0;;
let z = x;;
x := 4;;
!z;;

(** Exercice 2 **)
let a = ref 1;;
let f x = x + !a;;
f 3;;
a := 4;;
f 3;;
let a = ref 3;;
(* a n'est plus le a qui préexistait *)
f 3;;


a := 10;;
f 3;;

(** Exercice 3 **)

(* Fonction copy: 'a array -> 'a array *)
let copy tab =
  let n = Array.length tab in
  if n = 0
  then [||]
  else
    let new_tab = Array.make n tab.(0) in
    for i = 1 to n-1 do
      new_tab.(i) <- tab.(i)
    done;
    new_tab
;;

(* Fonction sub: 'a array -> int -> int -> 'a array
sub tab i k renvoie la portion de tableau qui démarre à l'indice i et de longueur k *)
let sub t i k =
  if i < 0 || i+k-1 >= Array.length t - 1
  then [||] (* Fort sympathique *)
  else
    let subt = Array.make k tab.(i) in
    (* subt.(0), 1er élément de subt, est t.(i)
subt.(1) est t.(i+1),
subt.(2) est t.(i+2),
...
subt.(k-1) est t.(i+k-1)
     *) 
    for j = i+1 to i+k-1 do      
      subt.(j-i) <- t.(j)
    done;
    subt
;;

(* Fonction mem: 'a -> 'a array -> bool
test appartenance *)
let mem e tab =
  let a = ref false in
  for i = 0 to Array.length tab - 1
  do
    if tab.(i) = e
    then
      a := true
  done;
  !a
;;
(* mais on continue si on a trouvé....*)

let mem e tab =
  let i = ref 0 in
  let n = Array.length tab in
  while !i < n && tab.(!i) <> e do
    i := !i + 1
  done;
  (* Deux raisons possibles de sortir de la boucle :
- ou bien !i >= n : on est arrivé au bout du tableau sans trouver e, il faudra renvoyer false
- ou bien !i < n mais tab.(!i) = e, il faut renvoyer true
*)
  !i < n
;;


(* Fonction map : ('a -> 'b) -> 'a array -> 'b array
map f [|t0;t1;...|] renvoie [|f(t0);f(t1);...|] *)

let map f tab =
  let n = Array.length tab in
  if n = 0
  then [||]
  else
    let ftab = Array.make n (f tab.(0)) in
    for i = 1 to n-1 do
      ftab.(i) <- f tab.(i)
    done;
    ftab
;;

(* append: 'a array -> 'a array -> 'a array
concaténation *)
