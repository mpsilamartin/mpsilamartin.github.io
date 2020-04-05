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

let a = ref 0;;
(* ATTENTION : on crée un nouvel objet qui s'appelle a *)
f 3;;

let a = ref "toto";;

(** Exercice 3 **)

(*Q1*)
(* copy : 'a array -> 'a array *)
let copy tab =
  let n = Array.length tab in
  if n = 0
  then [||]
  else
    let t = Array.make n tab.(0) in
    for i = 1 to n-1 do
      t.(i) <- tab.(i)
    done;
    t
;;
  

(*Q2*)
(* Fonction sub: 'a array -> int -> int -> 'a array
sub tab i k renvoie la portion de tableau qui démarre à l'indice i et de longueur k *)

let sub t i k =
  (* On pourrait faire des vérifications sur les indices avec d'éventuels failwith *)
  let t2 = Array.make k t.(i) in
  for j = 1 to (k-1) do
    t2.(j) <- t.(i+j)
  done;
  t2
;;

(*Q3*)
(* Fonction mem: 'a -> 'a array -> bool
test appartenance *)
let mem el tableau =
  let i = ref 0 and flag = ref false in
  while (not !flag) && !i < Array.length tableau do
    if tableau.(!i) = el
    then flag := true
    else i := !i + 1
  done;
  !flag
;;

let mem e tab =
  let n = Array.length tab in
  let i = ref 0 in
  while !i < n && tab.(!i) <> e do
    i := !i + 1
  done;
  (* On sort de la boucle lorsque la condition de boucle n'est plus vérifiée i.e lorsque 
- soit !i est supérieur ou égal à n : on est arrivé au bout du tableau sans trouver e
- soit !i < n mais tab.(!i) vaut e : on a trouvé e*)
  !i < n
;;

(*Q4*)
(* Fonction map : ('a -> 'b) -> 'a array -> 'b array
map f [|t0;t1;...|] renvoie [|f(t0);f(t1);...|] *)

let map f tab =
  let n = Array.length tab in
  if n = 0
  then [||]
  else
    let t = Array.make n (f tab.(0)) in
    for i = 1 to n-1 do
      t.(i) <- (f tab.(i))
    done;
    t
;;
  


(*Q5*)
(* Fonction append : 'a array -> 'a array -> 'a array
Concatène deux tableaux *) 
let append t1 t2 =
  let l1 = Array.length t1
  and l2 = Array.length t2
  in
  let t = Array.make (l1+l2) t1.(0) in
  for k = 1 to l1-1 do
    t.(k) <- t1.(k)
  done;
  for k = 0 to l2-1 do
    t.(k+l1) <- t2.(k)
  done;
  t;;
