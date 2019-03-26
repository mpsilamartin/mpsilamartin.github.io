(* Représentation d'une permutation *)
let est_permutation tab =
  let n = Array.length tab in
  let valeurs = Array.make n false in
  let i = ref 0 in
  let ok = ref true in
  while !ok && !i < n do
    let k = tab.(!i) in
    if k < 0 || k >= n || valeurs.(k)
    then ok := false
    else      
      begin
        valeurs.(k) <- true ;
        incr i
      end
  done;
  !ok
;;

let support tab =
  let s = ref [] in
  let n = Array.length tab in
  for i = n-1 downto 0 do
    if tab.(i) <> i
    then s := i::!s
  done;
  !s
;;

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

(* A compléter *)
let rec trie_droite t k = ()
;;
