(** Représentation d'une permutation **)
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
        t.(i)
        <- t1.(t2.(i))
      done;
      t
    end
    ;;

(** Enumération des permutations **)
exception TableauDecroissant;;

let indice_max_croit t =
  let n = Array.length t in
  let i = ref (n-2) in
  while !i >= 0 && t.(!i) >= t.(!i+1) do
    decr i
         (* équivalent à i := !i - 1 *)
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
  if k < n
  then
    begin
      let i = indice_min t k in
      echange t i k;
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
  let tab = Array.make n 0 in
  (* On démarre avec 0 1 2 3 ... n-1 *)
  for i = 1 to n-1 do
    tab.(i) <- i
  done ;
  print_perm tab;
  try
    while true do
      suivant tab;
      print_perm tab
    done
  with
  | TableauDecroissant -> print_string("Fini !") ;  print_newline()
;;

(** Cycles **)
let compose_cycle c t =
  match c with
  | [] -> ()
  | a::q ->
     let sigma_a = t.(a) in
     let rec applique lst =
       match lst with
       | [] -> () 
       | [b] -> t.(b) <- sigma_a
       | b::d::q -> t.(b) <- t.(d) ; applique (d::q)
     in applique c
;;

let produit_cycles lst n =
  let tab = Array.make n 0 in
  for i = 1 to n-1 do
    tab.(i) <- i
  done;
  let rec applique_cycles lc =
    match lc with
    | [] -> ()
    | c::q -> applique_cycles q ; compose_cycle c tab
  in
  applique_cycles lst;
  tab
;;

let q10c = [[0; 4; 2; 7]; [1; 6; 3]];;
produit_cycles q10c 8;;

let cycles tab =
  let n = Array.length tab in
  (* Le tableau vus permet de marquer les éléments qui sont déjà dans un cycle *)
  let vus = Array.make n false in
  (*La fonction trouve_cycle permet de construire le cycle commençant par l'élément debut *)
  let rec trouve_cycle debut courant  =
    vus.(courant) <- true ;
    let suivant = tab.(courant) in
    if suivant = debut
    then [courant]
    else courant::(trouve_cycle debut suivant)
  in
  let produit = ref [] in
  (* On construit le cycle auquel appartient chaque élément qui n'est pas un point fixe et qui n'a pas encore été vu *)
  for i = 0 to n-1 do
    if tab.(i) <> i && not vus.(i)
    then produit := (trouve_cycle i i)::!produit
  done;
  !produit
;;

let q10t = [|4; 6; 7; 1; 2; 5; 3; 0|];;
cycles q10t;;
