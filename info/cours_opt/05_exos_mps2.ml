let t = [|"hkjjlk"; "jhjkjhgf"; "pojhuk" |]

let copy t =
  let n = Array.length t in
  match n with
  | 0 -> [||]
  |_ -> let t2 = Array.make n t.(0) in
        for i = 1 to (n-1)
        do t2.(i) <- t.(i)
        done;
        t2
;;
let copy t =
  match t with
  | [||] -> [||]
  | _ ->
     let n = Array.length t in
     let t2 = Array.make n t.(0) in
     for i = 1 to (n-1)
     do t2.(i) <- t.(i)
     done;
     t2
;;

let sub t i k =
  match k with
  | 0 -> [||]
  | _ -> let g = Array.make k t.(i) in
         for l = i to i+k-1
         do g.(l-i) <- t.(l)
         done;
         g
;;

let mem x t =
  let n = Array.length t in
  let rec aux i =
    if i >= n
    then
      false
    else
      if t.(i) = x
      then true
      else aux (i+1)
  in aux 0
;;

(* Pas bien : *)
let mem x t =
  let n = Array.length t in
  let trouve = ref false in
  for i = 0 to (n-1)
  do
    if x = t.(i)
    then trouve := true
  done;
  !trouve
;;

(* Mieux *)
let mem x t =
  let n = Array.length t in
  let trouve = ref false in
  let i = ref 0 in
  while not !trouve && !i < n
  do
    if t.(!i) = x
   then trouve := true
    else incr i
  done;
  !trouve
;;
    
let mem x t =
  let n = Array.length t in
  let i = ref 0 in
  while !i < n && t.(!i) <> x
  do
    incr i
  done;
  !i < n
;;
    
let map f t =
  let n = Array.length t in
  match n with
  | 0 -> [||]
  | _ -> 
     let t2 = Array.make n (f t.(0)) in
     for i = 1 to n-1
     do
       t2.(i) <- f t.(i)
     done;
     t2
;;
