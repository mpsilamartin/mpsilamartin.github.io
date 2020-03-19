let rec fact n =
  if n = 0
  then 1
  else n * fact (n-1)
;;

let rec length l = 
  match l with 
  | [] -> 0
  | t::q -> 1 + length q
;;

let rec ack n p =
  match (n, p) with
  | 0, _ -> p+1
  | _, 0 -> ack (n-1) 1
  | _, _ -> ack (n-1) (ack n (p-1))
;;

let rec syracuse n =
  match n with 
  | 1 -> 1
  | _ -> if n mod 2 = 0
         then syracuse (n/2)
         else syracuse (3*n+1)
;;


let rec somme n=
  if n = 0
  then 0
  else n + somme (n-1)
;;

let rec somme_avec_acc n acc =
  match n with
  | 0 -> acc
  | _ -> somme_avec_acc (n-1) (n+acc)
;;


let somme n =
  somme_avec_acc n 0
;;

let somme n =
  let rec aux n acc =
    match n with
    | 0 -> acc
    | _ -> aux (n-1) (n+acc)
  in aux n 0
;;

