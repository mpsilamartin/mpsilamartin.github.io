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

let tri_selection t =
  let n = Array.length t in
  for k = 0 to n-2 do
    (* n-1 itérations : k = 0 à n-2*)
    let j = ref k in
    for i = k+1 to n-1 do
      (* n-1-k itérations *)
      (* donc on effectue (n-1)+ (n-2) + ..+1 fois ce qui suit qui est en temps O(1)*)
      if t.(i) < t.(!j)
      then j := i
    done;
    echange t !j k (* Echange en O(1) *)
  done
;;
(* Complexité : O(n²) *)

(* Tri selection min *)
let tri_selection t =
  let n = Array.length t in
  for j = 0 to n-1 do
    (* Recherche de l'élément min à partir de l'indice j *)
    let min = ref t.(j) in
    let indice = ref j in
    for i = j to n-1 do
      if !min > t.(i)
      then
	begin
	  min := t.(i);
	  indice := i
	end
    done;
    (* On échange l'élément d'indice j avec le min trouvé *)
    t.(!indice) <- t.(j);
    t.(j) <- !min
  done;
;;

(* Tri selection max *)
let tri_selection t=
  let n=ref (Array.length t) (* longueur de la portion considérée *)
  in (* Indice du max trouvé dans la portion *)
  while !n>=2 do
    let s = ref 0 in
    for i=1 to !n-1 do
      if t.(!s)<t.(i)
      then s:=i
    done;
    let a= t.(!n-1) in
    (* On échange les éléments d'indice !n-1 et !s *)
    t.(!n-1)<-t.(!s);
    t.(!s)<- a;
    (* On met à jour n *)
    n:=!n-1;
  done;
;;




(*Exo 5*)

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
(* Complexité : O(n²)*)

let tri_insertion t =
  let n = Array.length t in
  for j = 1 to n-1 do
    let indice = ref j in
    let var = t.(j) in
    if t.(j) <= t.(0) then
      begin
        (* On décale tout à droite jusqu'à l'indice j pour mettre t.(j) au début *)
        for i = j-1 downto 0 do
	  t.(i+1)<-t.(i)
        done;
        t.(0)<-var
      end
    else
      begin
        (* On cherche l'indice i où il faut mettre t.(j) *)
        for i = 0 to j-1 do
	  if t.(j)> t.(i) && t.(j) <= t.(i+1)
          then indice := i+1
        done; 
        (* On décale à droite jusqu'à l'indice j pour "libérer" l'indice indice *)
        for i = j-1 downto !indice  do
          t.(i+1)<-t.(i)
        done;
        t.(!indice)<-var
      end
  done
;;


