(** Chemin dans une matrice **)
(* Algorithme naïf *)

let rec smin m i j =
  match (i, j) with
  | (0, 0) -> m.(0).(0)
  | (0, _) -> smin m 0 (j-1) + m.(0).(j)
  | (_, 0) -> smin m (i-1) 0 + m.(i).(0)
  | _ -> min (smin m (i-1) j)
           (smin m i (j-1)) + m.(i).(j)
;;

let m1 = [| [| 131 ; 673 ; 234 ; 103 ; 18 |];
            [| 201 ; 96 ; 342 ; 965 ; 150 |];
            [| 630 ; 803 ; 746 ; 422 ; 111 |];
            [| 537 ; 699 ; 497 ; 121 ; 38 |];
            [| 805 ; 732 ; 524 ; 37 ; 331 |]
         |];;
smin m1 4 4;;
let n, p = 15, 15;;
let m = Array.make_matrix n p 0;;
for i = 0 to n-1 do
  for j = 0 to p-1 do
    m.(i).(j) <- (i+1)*(2*j+1)
  done
done;;
smin m (n-1) (p-1);;


let rec compl i j =
  match (i, j) with
  | (0, 0) -> 1
  | (0, _) -> 1 + compl 0 (j-1)
  | (_, 0) -> 1 + compl (i-1) j
  | _ -> 1 + compl (i-1) j + compl i (j-1)
;;



(* Mémoïsation *)
let rec smin t m i j =
  if t.(i).(j) >= 0
  then t.(i).(j)
  else
    let res = match (i,j) with
      | (0, 0) -> m.(0).(0)
      | (0, _) -> smin t m 0 (j-1) + m.(0).(j)
      | (_, 0) -> smin t m (i-1) 0 + m.(i).(0)
      | _ -> min (smin t m (i-1) j) (smin t m i (j-1)) + m.(i).(j)
    in
    t.(i).(j) <- res;
    res
;;
let t = Array.make_matrix n p (-1);;

smin t m (n-1) (p-1);;

(* Calcul itératif *)

let rec smin_it m =
  let n = Array.length m in
  let p= Array.length m.(0) in
  let t = Array.make_matrix n p (-1) in
  for i = 0 to n-1 do
    for j = 0 to p-1 do
      let res =
        match (i,j) with
        | (0,0) -> m.(0).(0)
        | (0, _) -> t.(0).(j-1) + m.(0).(j)
        | (_, 0) -> t.(i-1).(0) + m.(i).(0)
        | _ -> min t.(i-1).(j) t.(i).(j-1) + m.(i).(j)
      in
      t.(i).(j) <- res
    done
  done;
  t
;;

(* Réduction de la complexité spatiale *)
let rec smin_it2 m =
  let n = Array.length m in
  let p= Array.length m.(0) in
  let t = Array.make p (-1) in
  for i = 0 to n-1 do
    for j = 0 to p-1 do
      let res =
        match (i,j) with
        | (0,0) -> m.(0).(0)
        | (0, _) -> t.(j-1) + m.(0).(j)
        | (_, 0) -> t.(0) + m.(i).(0)
        | _ -> min t.(j) t.(j-1) + m.(i).(j)
      in
      t.(j) <- res
    done
  done;
  t.(p-1)
;;
