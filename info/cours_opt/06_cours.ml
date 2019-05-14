(*Exponentation rapide*)
let rec puissance x n =
  match n with
  | 0 -> 1
  | 1 -> x
  | _ -> if n mod 2 = 0
         then puissance (x*x) (n/2)
         else x * puissance (x*x) (n/2)
;;

(*Tri fusion*)
let rec decoupe l =
  match l with
  | [] -> [], []
  | [x] -> [x], []
  | t1::t2::q -> let q1, q2 = decoupe q in
		 t1::q1, t2::q2
;;

let rec fusion l1 l2 =
  match (l1, l2) with 
  | _, [] -> l1
  | [], _ -> l2
  | t1::q1, t2::q2 -> if t1<t2
		      then t1::(fusion q1 l2)
		      else t2::(fusion l1 q2)
;;

let rec tri_fusion l =
  match l with
  | [] -> []
  | [x] -> [x]
  | _ -> let l1, l2 = decoupe l in
	 fusion (tri_fusion l1) (tri_fusion l2)
;;

(* Tri rapide *)
let partition p l =
  let l1 = List.filter (fun x -> x <= p) l in
  let l2 = List.filter (fun x -> x > p) l in
  (l1, l2)
;;

let rec quicksort l =
  match l with
  | [] -> []
  | t::q -> let (l1, l2) = partition t q in
            let l1t = quicksort l1 in
            let l2t = quicksort l2 in
            l1t@(t::l2t)
;;
