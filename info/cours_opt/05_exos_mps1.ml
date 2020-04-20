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


(** Exercice 4 **)
let tri_selection tab=
  let n=Array.length tab in
  for k= 0 to n-1 do
    let i_min= ref k in
    for i = k+1 to n-1 do
      if tab.(!i_min)>tab.(i)
      then i_min := i
    done;
    let tmp = tab.(k) in
    tab.(k)<-tab.(!i_min);
    tab.(!i_min) <- tmp
  done
;;
(** Tri selection **)
(* La fonction suivante echange les elements 
d'indice i et j dans le tableau t *)
let echange t i j =
  let tmp = t.(i) in
  t.(i) <- t.(j);
  t.(j) <- tmp
;;

(* Renvoie l'indice du ppe a partir de l'indice i*)
let rec indice_min t i =
  let n = Array.length t in
  if i = n-1
  then n-1
  else let j = indice_min t (i+1) in
       if t.(j) < t.(i)
       then j
       else i
;;

let tri_selection t =
  let n = Array.length t in
  let rec trie_droite t k =
    if k < n-1
    then 
      let i = indice_min t k in
      echange t i k;
      trie_droite t (k+1)
  in
  trie_droite t 0
;;


(* Exercice 5 *)

(** Tri insertion **)
let tri_insertion t =
  let n = Array.length t in
  for i = 1 to n-1 do
    (* n-1 itérations *)
    let j = ref i in
    (* Dans le pire des cas, dans la boucle suivante,
j atteint 0, il y a dans le pire des cas i itérations, i est majoré par n-1 *)
    while !j > 0 && t.(!j) <t.(!j-1) do
      (* Deux instructions en O(1) *)
      echange t !j (!j-1);
      decr j (*j := !j - 1*)
    done
  done
;;

let tri_insertion tab=
  let n=Array.length tab in
  for i= 0 to n-2 do
    (* est-ce que tab.(i+1) n'est pas à sa place *)
    if tab.(i)>tab.(i+1)
    then
      (* On cherche le plus petit j tq tab.(i) <= tab.(!j) *)
      let j=ref 0 in
      while tab.(i+1)>tab.(!j)do
        j := !j +1
      done;      
      (* On doit mettre tab.(i) à la place de tab.(!j) en décalant tout vers la droite *)
   let mem=tab.(i+1) in
    for k = i downto !j do
      tab.(k+1)<-tab.(k)
    done;
    tab.(!j)<-mem
  done;
;;

(*Ex6*)
(* Deux polynômes P et Q représentés par 
[|a0;a1;..;an|] et [|b0;b1;...;bm|] *)
(* On doit faire une fonction qui renvoie le tableau qui correspond à la somme *)


let add t1 t2=
  let n1 = Array.length t1 in
  let n2 = Array.length t2 in
  let n = max n1 n2 in
  let somme = Array.make n (t1.(0)+t2.(0))  in
  for i = 1 to n1-1 do
    somme.(i) <- t1.(i)
  done;
  for i = 1 to n2-1 do
    somme.(i) <- somme.(i) + t2.(i)
  done;
  somme;;
  

  
