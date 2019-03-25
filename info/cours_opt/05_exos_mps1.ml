let copy l =
  let n = Array.length l in
  if n = 0
  then [||]
  else
    let t = Array.make n l.(0) in
    for i = 1 to (n-1) do
      t.(i) <- l.(i)
    done;
    t
;;

let sub t i k =
  if k = 0
  then [||]
  else
    let j = Array.make k t.(i) in
    for m = 1 to k-1 do
      j.(m) <- t.(i+m)
    done;
    j
;;


let mem x t =
  let n = Array.length t in
  let trouve = ref false in
  let k = ref 0 in
  while !k < n && not !trouve do
    if t.(!k) = x
    then trouve := true
    else incr k
  done;
  !trouve
;;

let mem x t =
  let n = Array.length t in
  let k = ref 0 in
  while !k < n && t.(!k) <> x do
    incr k
  done;
  !k < n
;;

let mem x t =
  let rec aux x t k =
    if k >= Array.length t
    then false
    else
      if t.(k) = x
      then true
      else aux x t (k+1)
  in
  aux x t 0
;;

let append t1 t2 =
  let n1 = Array.length t1 in
  let n2 = Array.length t2 in
  if n1 + n2 = 0
  then [||]
  else
    let t = Array.make (n1+n2)
              (if n1 = 0 then t2.(0) else t1.(0))
    in
    for i = 1 to (n1+n2-1) do
      if i < n1
      then t.(i) <- t1.(i)
      else t.(i) <- t2.(i-n1)
    done;
    t
;;

(* Tri selection *)

(* Echange en place les éléments d'indices i et j du tableau t *)
let echange t i j =
  let tmp = t.(i) in
  t.(i) <- t.(j);
  t.(j) <- tmp
;;

let tri_selection t =
  let n = Array.length t in
  for i = 0 to (n-2) do
    let z = ref i in
    for j = i+1 to n-1 do
      if t.(j) < t.(!z)
      then z := j
    done ;
    echange t i !z
  done
;;

(* Tri insertion *)

let tri_insertion t =
  let n = Array.length t in
  for i = 1 to n-1 do
    let j = ref i in
    while !j > 0 && t.(!j) < t.(!j-1) do
      echange t !j (!j-1);
      decr j
    done
  done
;;
