(* Q1 *)

(* Algorithme n°1 : on compare les éléments deux à deux pour vérifier qu'ils sont distincts *)

let est_permutation t =
  let pas_de_pb = ref true in
  let n = Array.length t in
  let i = ref 0 in
  while !pas_de_pb && !i < n
  do
    let j = ref (!i+1) in
    while !pas_de_pb && !j < n
    do
      if t.(!i) = t.(!j)
      then pas_de_pb := false
      else incr j
    done;
    incr i
  done;
  !pas_de_pb
;;

(* Algorithme n°2 : on regarde si on a les entiers de 0 à n-1 au moins une fois *)

let est_permutation t =
  let n = Array.length t in
  (* tval.(k) contient true ssi on a rencontré k *)
  let tval = Array.make n false in
  let pas_de_pb = ref true in
  let i = ref 0 in
  while !pas_de_pb && !i < n
  do 
    let k = t.(!i) in
    if k < 0 || k >= n || tval.(k)
    then
      (* k n'est pas compris entre 0 et n-1
ou a déjà été rencontré *)
      pas_de_pb := false
    else
      (* on incrémente i et on indique qu'on a vu k *)
      begin
	incr i;
	tval.(k) <- true
      end
  done;
  !pas_de_pb
;;

    
  
(* Q2 *)
(* Renvoie la liste des éléments du support *)

let support tab =
  let s = ref [] in
  let n = Array.length tab in
  for i = n-1 downto 0 do
    if tab.(i) <> i
    then s := i::!s
  done;
  !s
;;

(*Q3*)
let compose t1 t2 =
  let n = Array.length t1 in
  if n = 0
  then [||]
  else
    begin
      let t = Array.make n t1.(0) in
      for i = 0 to n-1 do
        t.(i) <- t1.(t2.(i))
      done;
      t
    end
;;

(* Enumération des permutations *)
exception TableauDecroissant;;

let indice_max_croit t =
  let n = Array.length t in
  let i = ref (n-2) in
  while !i >= 0 && t.(!i) >= t.(!i+1) do
    decr i
  done;
  if !i >=0
  then !i
  else raise TableauDecroissant
;;

(* La fonction suivante réalise l'échange en place des éléments d'indices i et j du tableau tab*)
let echange tab i j =
  let tmp = tab.(i) in
  tab.(i) <- tab.(j);
  tab.(j) <- tmp
;;

let permute_max t i =
  let n = Array.length t in
  let j = ref i in
  for k = i+1 to n-1 do
    if t.(k) > t.(i) && (t.(k) < t.(!j) || !j = i)
    then j := k
  done;
  echange t i !j
;;

(* La fonction suivante renvoie l'indice de l'élément minimal à partir de l'indice i inclus*)
let rec indice_min t i =
  let n = Array.length t in
  if i = n-1
  then n-1
  else let j = indice_min t (i+1) in
       if t.(j) < t.(i)
       then j
       else i
;;

let rec trie_droite t k =
  let n = Array.length t in
  if k < n-1
  then
    begin
      let imin = indice_min t k in
      echange t k imin;
      trie_droite t (k+1)
    end
;;

let suivant t =
  let i = indice_max_croit t in
  permute_max t i;
  trie_droite t (i+1)
;;

let print_perm t =
  let n = Array.length t in
  for i = 0 to n-1 do
    print_int t.(i);
    print_char ' '
  done;
  print_newline ()
;;

let enumere n =
  let t = Array.make n 0 in
  for i = 1 to n-1 do
    t.(i) <- i
  done;
  try
    while true do
      print_perm t;
      suivant t
    done
  with
  | TableauDecroissant -> print_string "Fini !!!"
;;

  (* Cycles *)

let compose_cycle c t =
  let rec aux c t c0 =
    match c with
    | [x] -> t.(x) <- c0
    | x1::x2::q -> t.(x1) <- t.(x2) ;
		   aux (x2::q) t c0
  in
  aux c t (List.hd c)
;;

let identite n =
  let t = Array.make n 0 in
  for i = 1 to n-1 do
    t.(i) <- i
  done;
  t
;;

